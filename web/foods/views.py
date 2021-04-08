from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodInfo, Food
from .forms import FoodCreateForm

from keras.applications import ResNet50, imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image
import numpy as np
import io
# Create your views here.

model = None
food_lst = ['가지볶음', '간장게장', '갈비구이', '갈비찜', '갈비탕', '갈치구이', '갈치조림', '감자전', '감자조림', '감자채볶음', '감자탕', '갓김치', '건새우볶음', '경단', '계란국', '계란말이', '계란찜', '계란후라이', '고등어구이', '고등어조림', '고사리나물', '고추장진미채볶음', '고추튀김', '곰탕_설렁탕', '곱창구이', '곱창전골', '과메기', '김밥', '김치볶음밥', '김치전', '김치찌개', '김치찜', ' 깍두기', '깻잎장아찌', '꼬막찜', '꽁치조림', '꽈리고추무침', '꿀떡', '나박김치', '누룽지', '닭갈비', '닭계장', '닭볶음탕', '더덕구이', '도라지무침', '도토리묵', '동그랑땡', '동태찌개', '된장찌개', '두부김치', '두부조림', '땅콩조림', '떡갈비', '떡국_만두국', '떡꼬치', '떡볶이', '라면', '라볶이', '막국수', '만두', '매운탕', '멍게', '메추리알장조림', '멸치볶음', '무국', '무생채', '물 냉면', '물회', '미역국', '미역줄기볶음', '배추김치', '백김치', '보쌈', '부추김치', '북엇국', '불고기', '비빔냉면', '비빔밥', '산낙지', '삼겹살', '삼계탕', '새우볶음밥', '새우튀김', '생선전', '소세지볶음', '송편', '수육', '수정과', '수제비', '숙주나물', '순대', '순두부찌개', '시금치나물', '시래기국', '식혜', '알밥', '애호박볶음', '약과', '약식', '양념게장', '양념치킨', '어묵볶음', '연근조림', '열무국수', '열무김치', '오이소박이', '오징어채볶음', '오징어튀김', '우엉조림', '유부초밥', '육개장', '육회', '잔치국수', '잡곡밥', '잡채', '장어구이', '장조림', '전복죽', '젓갈', '제육볶음', '조개구이', '조기구이', '족발', '주꾸미볶음', '주먹밥', '짜장면', '짬뽕', '쫄면', '찜닭', '총각김치', '추어탕', '칼국수', '코다리조림', '콩국수', '콩나물국', '콩나물무침', '콩자반', '파김치', '파전', '편육', '피자', '한과', '해물찜', '호박전', '호박죽', '홍어무침', '황태구이', '회무침', '후라이드치킨', '훈제오리']


def index(request):
    if request.user.is_authenticated:
        food_infos = FoodInfo.objects.filter(user=request.user.pk).order_by('-pk')
        print(request.user.hateingredient.all())
        context = {'food_infos':food_infos}
        return render(request, 'foods/index.html', context)
    return render(request, 'foods/index.html')

def _image_prepare(image, target):
    
    if image.mode != 'RGB':
        image = image.conver('RGB')
    image = image.resize(target)
    image = np.asarray(image).astype(np.float32)/255
    image = np.expand_dims(image, axis=0)
    # image = imagenet_utils.preprocess_input(image)

    return image

def load():
    global model
    model = load_model('keras/08_5301.h5')

def create(request):
    global food_lst
    if request.user.is_authenticated:
        if request.method == 'POST':
            

            img = request.FILES.get('img')
            img = Image.open(img)
            img = _image_prepare(img, (224,224))
            
            load()
            
            pred = model.predict(img)
            result = pred.argmax()
            food = Food.objects.get(name=food_lst[result])
            print(food.name)
            foodinfo = FoodInfo(img=request.FILES.get('img'), food=food, user=request.user)
            foodinfo.save()
            return redirect('foods:index')
    return redirect('foods:index')

from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodInfo
from .forms import FoodCreateForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            # foods = FoodInfo.objects.filter(user=request.user.pk).order_by('-pk')
            context = {'test':[1,2,3,4,5,6,7,7,7,7]}
            print(context)
            return render(request, 'foods/index.html', context)
        except:
            pass

    return render(request, 'foods/index.html')

def create(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FoodCreateForm(request.POST, request.FILES)
            ## 모델 불러와서 음식 보여주기.
            return redirect('foods:index')
            
            if form.is_valid():
                review = form.save()
                print('save')
                return redirect('foods:index')
    return redirect('foods:index')


def detail(request):

    return render(request)


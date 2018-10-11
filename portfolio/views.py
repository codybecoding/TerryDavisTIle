from django.shortcuts import render
from .models import FlooringPic, ShowerPic, KitchenPic, BathtubPic, FireplacePic, CountertopPic
import random


# Create your views here.
def portfolio_index(request):
    return render(request, 'portfolio.html')


def floor_index(request):
    object_list = FlooringPic.objects.all()
    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'flooring.html', context)


def shower_index(request):
    object_list = ShowerPic.objects.all()

    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'showers.html', context)


def kitchen_index(request):
    object_list = KitchenPic.objects.all()
    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'kitchens.html', context)


def bathtub_index(request):
    object_list = BathtubPic.objects.all()
    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'bathtubs.html', context)


def fireplace_index(request):
    object_list = FireplacePic.objects.all()
    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'fireplace.html', context)


def countertop_index(request):
    object_list = CountertopPic.objects.all()
    context = {
        'object_list': object_list[::-1]
    }
    return render(request, 'countertops.html', context)


# def random_pictures(request):
#     random_list = list(FireplacePic.objects.all()) + list(BathtubPic.objects.all()) + list(KitchenPic.objects.all()) + list(ShowerPic.objects.all()) + list(FlooringPic.objects.all()) + list(CountertopPic.objects.all())

#     object_list = []

#     for random_img in range(3):
#         randy = random.randint(0, len(random_list) - 1)
        
#         object_list.append(randy)

#     context = {
#     'object_random': object_list
#     }

#     return render(request, 'home.html', context)
        



    
from django.shortcuts import render, get_object_or_404
from .models import Product, Picture, PricePackage
from userprofiles.models import Profile

def homepage(request):
    profiles = Profile.objects.all()
    picture1 = Picture.objects.get(pk=2)
    picture2 = Picture.objects.get(pk=1)
    product = Product.objects.get(pk=1)
    starter = PricePackage.objects.get(pk=1)
    most_popular = PricePackage.objects.get(pk=2)
    ultimate = PricePackage.objects.get(pk=3)
    context = {'product': product, 'profiles':profiles, 
               'picture1':picture1, 
               'picture2':picture2,
               'starter':starter, 
               'most_popular':most_popular,
               'ultimate':ultimate,
               }
    return render(request, "base/index.html", context)

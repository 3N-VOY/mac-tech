from django.contrib import admin
from .models import Product, Picture, PricePackage

admin.site.register(Product)
admin.site.register(Picture)
admin.site.register(PricePackage)
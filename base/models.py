from django.db import models

class Picture(models.Model):
    picture  = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def get_image(self):
        if self.picture:
            return self.picture.url

class PricePackage(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.FloatField()
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ManyToManyField(Picture, blank=True)
    price_packages = models.ManyToManyField(PricePackage, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return self.image


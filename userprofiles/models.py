from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    birth_date = models.DateField(null=True, blank=True)
    review = models.TextField(max_length=500, blank=True)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    profile_picture = models.ImageField(upload_to='userprofiles/', blank=True, null=True)
    job_title = models.CharField(max_length=55, blank=True)

    
    
    
    def __str__(self):
        
        return self.user.email
    
    
    def get_profile_pic(self):
        if self.profile_picture:
            return self.profile_picture.url
    
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
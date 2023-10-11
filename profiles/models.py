from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.URLField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return f'Profile owned by {self.user.username}'
    
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        
post_save.connect(create_user_profile, sender=User)
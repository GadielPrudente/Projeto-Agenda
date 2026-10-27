from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'



    name = models.CharField(max_length=50)

    
    def __str__(self) -> str:
        return self.name

    
class Contact(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, blank=True)
    Creatd_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                                 blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.First_name} {self.Last_name}'
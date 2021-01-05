from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class categories(models.Model):
    cat_name = models.CharField(max_length=35)
    cat_img = models.ImageField()
    cat_desc = models.TextField()

    def __str__(self):
        return self.cat_name


class desserts(models.Model):
    des_name = models.CharField(max_length=35)
    des_img = models.ImageField()
    des_country = models.CharField(max_length=25)
    des_instr = models.TextField()
    des_ingreds = models.TextField()
    des_ingamt = models.TextField()
    des_youtube = models.TextField()
    des_source = models.TextField()

    def __str__(self):
        return self.des_name
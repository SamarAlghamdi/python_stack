from django.db import models


# Create your models here.
class Dojos(models.Model):
    name= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    desc=models.CharField(max_length=255,default="old dojo")

    def ninja_count(self):
        return self.ninja.count()

class Ninjas(models.Model):
    dojo_id= models.ForeignKey(Dojos,related_name="ninja",on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)


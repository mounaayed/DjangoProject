from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    
# Create your models here.
class Product(models.Model):
    name=models.CharField('namee',max_length=50)  #string type #par default kol not null w id yegenera wa7dou w namee label
    price=models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True) #detecter date systeme et l inserer 
    updated_at=models.DateField(auto_now=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True)

  
#fil html tenajem teged ba3ed | date : 'Y-m-d' ki tebda 3andek date
# zedé {{ a| length}} ya3tik nb
# EmailField,FileField,DateField,IntegerField


# • On distingue 3 types d’associations:
# – « One-to-One »
# – « Many-to-One »
# – « Many-to-Many »
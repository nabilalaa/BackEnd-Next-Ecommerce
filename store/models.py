from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/", blank=True)
    image_Url =  models.URLField(null=1,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categorie'


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/", blank=True)
    urlImage = models.URLField(null=1,verbose_name="url image")
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey("category", on_delete=models.DO_NOTHING, null=1,blank=True)

    def __str__(self):
        return self.name




class Cart (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,related_name="items")


    def __str__(self):
        return self.product.name
    



class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    notes = models.TextField(null=True)
    products = models.TextField(null=True)

    def __str__(self):
        return self.name

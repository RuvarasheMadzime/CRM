from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 50)
    last_name =models.CharField(max_length = 50)
    email =models.CharField(max_length = 100)
    phone =models.CharField(max_length = 20)
    address =models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state =models.CharField(max_length = 50)
    zipcode =models.CharField(max_length = 20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
class Product(models.Model):
    ItemId=models.CharField(max_length = 50)
    ProductType=models.CharField(max_length = 50)#dress,jean,jacket etc
    category=models.CharField(max_length = 50)#Men,Women,Kids
    price=models.IntegerField()
    description=models.CharField(max_length = 50)

    def __str__(self):
        return(f"{self.ItemId} {self.price}")
    

    




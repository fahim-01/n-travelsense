from django.db import models

# Create your models here.
    
class Destination(models.Model ):
    Dest_id = models.AutoField
    Destination_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")  
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="images", default="0")
    desc = models.CharField(max_length=6000)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.Destination_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=10000, default="")


    def __str__(self):
        return self.name



class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    departure = models.CharField(max_length=100, default="")
    destination = models.CharField(max_length=100, default="")
    number_of_guests = models.CharField(max_length=100, default="")    
    phone = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=10000, default="")



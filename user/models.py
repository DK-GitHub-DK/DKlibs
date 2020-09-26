from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genre(models.Model):
    GenreName = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.GenreName

class Books(models.Model):
    status = (('unavailable','unavailable'),('available','available'))
    BookName = models.CharField(max_length = 200, null=True)
    AuthorName = models.CharField(max_length = 200, null=True)
    Status =  models.CharField(max_length = 200, null=True, choices = status)
    Genre = models.ManyToManyField(Genre)
    Age = models.CharField(max_length = 10, null = True)
    Image = models.ImageField(null = True, blank =True, upload_to = 'books/images')
    PDF = models.FileField(null = True, blank =True, upload_to = 'books/pdfs')
    Description = models.TextField(null = True, blank = True)
    Note = models.CharField(max_length = 500, null = True, blank = True)

    def __str__(self):
        return self.BookName

class Customer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    PhoneNo = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    Address = models.CharField(max_length = 10, null = True)
    DatePayed = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    status = (('delivering','delivering'),('delivered','delivered'),('returning','returning'),('returned','returned'))
    date_created = models.DateField(auto_now_add = True, null =True)
    Customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    Product = models.ForeignKey(Books, null = True, on_delete = models.SET_NULL)
    Status =  models.CharField(max_length = 200, null=True, choices = status)
    recieved_on = models.DateField(null =True, blank = True)
    returned_on = models.DateField(null =True, blank = True)

    def __str__(self):
        return str(self.Customer.name)+' , '+str(self.Product.BookName)

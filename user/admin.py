from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Customer)
admin.site.register(Orders)

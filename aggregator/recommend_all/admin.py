from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Music)
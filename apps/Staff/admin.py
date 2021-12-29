from django.contrib import admin

# Register your models here.
from apps.Staff.models import UserModel

admin.site.register(UserModel)
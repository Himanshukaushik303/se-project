from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Shop)
admin.site.register(Order)
admin.site.register(Subscription)
admin.site.register(Product)
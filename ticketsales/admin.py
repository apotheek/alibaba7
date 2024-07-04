from django.contrib import admin
from .models import login_user,login_Admin,Category,Attribute,Price_Alibaba,CategoryAttribute,Trip,TripAttribute,Passenger,Tiket,Factor


# Register your models here.
admin.site.register(login_user)
admin.site.register(login_Admin)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Price_Alibaba)
admin.site.register(CategoryAttribute)
admin.site.register(Trip)
admin.site.register(TripAttribute)
admin.site.register(Passenger)
admin.site.register(Tiket)
admin.site.register(Factor)


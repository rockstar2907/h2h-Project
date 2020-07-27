from django.contrib import admin
from users.models import UserDetails,Restaurants,Items,AllOrders,CurrentOrders,UserOrders,Cart
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Restaurants)
admin.site.register(Items)
admin.site.register(Cart)
admin.site.register(AllOrders)
admin.site.register(CurrentOrders)
admin.site.register(UserOrders)
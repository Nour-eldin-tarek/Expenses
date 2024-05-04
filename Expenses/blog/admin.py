from django.contrib import admin
from .models import user
from .models import bill
from .models import expenses
from .models import person
# from .models import user2



# Register your models here.

# admin.site.register(user)
@admin.register(user)
class user(admin.ModelAdmin):
    list_display=('id','f_name','email','join_date')
    ordering=('join_date','-id')
    search_fields=('email','id')

@admin.register(bill)
class bill(admin.ModelAdmin):
    list_display=('id','descrip','nanasha','user_id','join_date')
    ordering=('join_date','-id')
    search_fields=('descrip','join_date')

@admin.register(expenses)
class expenses(admin.ModelAdmin):
    list_display=('id','category','product_name','product_price','bill_id')
    ordering=('id','-product_price')
    search_fields=('category','product_name')

@admin.register(person)
class person(admin.ModelAdmin):
    list_display=('id','name','user_id')
    ordering=('id','-name')
    search_fields=('name',)

# @admin.register(user2)
# class user2(admin.ModelAdmin):
#     list_display=('id','f_name','l_name','join_date')
#     ordering=('join_date','-id')
#     search_fields=('f_name','id')
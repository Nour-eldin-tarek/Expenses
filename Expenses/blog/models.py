from django.db import models
from django.core.exceptions import ValidationError
# from django.core.validators import MinLengthValidator

# Create your models here.
def validate_min_length(value):
    if len(value) < 5:
        raise ValidationError('Password must be at least 5 characters long.')
    
class user(models.Model):
    # id = models.AutoField(primary_key=True) # in django the id is atumatic added
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    bassword = models.CharField(max_length=20, validators=[validate_min_length])
    join_date = models.DateTimeField(auto_now_add=True)

class bill(models.Model):
    descrip = models.TextField(default='مشتريات')
    nanasha = models.FloatField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    nameOfBuyer = models.CharField(max_length=15)
    user_id=models.ForeignKey(user, on_delete=models.CASCADE, to_field='id')

class expenses(models.Model):
    category = models.CharField(max_length=15)
    product_name = models.CharField(max_length=15)
    product_price = models.FloatField()
    bill_id=models.ForeignKey(bill, on_delete=models.CASCADE, to_field='id')

def uniqunameforuser(instance):
    existing_names = person.objects.filter(name=instance.name, user_id=instance.user_id)
    if instance.pk is not None:
        existing_names = existing_names.exclude(pk=instance.pk)  # Exclude the current instance if it's being edited
    if existing_names.exists():
        raise ValidationError('This name is already associated with your user_id.')


class person(models.Model):
    name = models.CharField(max_length=15)
    user_id=models.ForeignKey(user, on_delete=models.CASCADE, to_field='id')
    def clean(self):
        uniqunameforuser(self)

# class user2(models.Model):
#     id = models.AutoField(primary_key=True) # in django the id is atumatic added
#     f_name = models.CharField(max_length=15)
#     l_name = models.CharField(max_length=15)
#     join_date = models.DateTimeField(auto_now_add=True)
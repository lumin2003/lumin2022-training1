from django.db import models


# Create your models here.
# GENDER_CHOICES= ( (0, 'male'), (1, 'female'), (2, 'not specified') )

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    create_date = models.DateField()
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=6 )
    #choose_file=models.CharField(max_length=50)


class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_address = models.CharField(max_length=500)
    user_email = models.EmailField()
    user_age = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=6)
    user_cards = models.CharField(max_length=20)
    user_numbers = models.CharField(max_length=20)







from django.shortcuts import render

# Create your views here.
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def create_user_random(quantity):
    for x in range(quantity):
        username = 'user_{}'.format(get_random_string(5, string.ascii_letters))
        email = '{}@company.com'.format(username)
        password = get_random_string(50)
        User.objects.create(username=username, email=email, password=password)
    return '{} Users created'.format(x) 
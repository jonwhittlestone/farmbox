from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.db import transaction


def user_allowed(client, username='fred', email='fred@example.com', password='password'):
    user = create_user(username=username, email=email, password=password)
    client = login_user(client, username=username, password=password)
    return user, client

def create_user(username='fred', email='fred@example.com', password='password'):
    User = get_user_model()
    try:
        with transaction.atomic():
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.is_staff = True
            user.save()
    except IntegrityError:
        user = User.objects.get(username=username)
    return user

def login_user(client, username='fred', password='password'):
    client.login(username=username, password=password)
    return client

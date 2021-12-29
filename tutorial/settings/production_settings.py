from tutorial.default_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TESTAPI',
        'USER': 'root',
        'PASSWORD': 'Password@123',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
#Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'survey',
	'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

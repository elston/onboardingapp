import os
import sys
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name, allow_none=False):
    try:
        return os.environ[var_name]
    except KeyError:
        if allow_none is False:
            err_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(err_msg)
        return None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SECRET_KEY = "eac*+7=6p-lk*n#mx(ro8%z(90kjw*#z^i86$w5ebv581kajqoze"
DEBUG = False

ALLOWED_HOSTS = ["server.domain"]
SERVER_HOST = get_env_variable('SERVER_HOST',True)
if SERVER_HOST:
    ALLOWED_HOSTS.append(SERVER_HOST)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'team',
    'services',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),        
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.static",                
            ],
        },
    },
]

ROOT_URLCONF = 'onboardingapp.urls'
WSGI_APPLICATION = 'onboardingapp.wsgi.application'
AUTH_USER_MODEL = 'team.TeamUser'

# Password validation
AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
},{
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
},]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Logging files
LOG_FILE = os.path.join(BASE_DIR, '.logs/django.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    }, 
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
        },
    },
    'loggers': {
        'onboardingapp': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': True,
            'formatter': 'standard',
        },
    },
}



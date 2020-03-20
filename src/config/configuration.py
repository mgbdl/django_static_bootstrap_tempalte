#########################
#                       #
#   Required Settings   #
#                       #
#########################

# Example: ALLOWED_HOSTS = ['netbox.example.com', 'netbox.internal.local']
ALLOWED_HOSTS = []

# Base URL path if aceesing Base within a directory.
BASE_PATH = ''

# PostgreSQL database configuration
DATABASE = {
    # 'NAME': '',
    # 'USER': '',
    # 'PASSWORD': '',
    # 'HOST': '',
    # 'PORT': '',
    # 'CONN_MAX_AGE': 300,
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dwpm9+k%$k(8686*6%-j9y_bhvsx7k7uexgsh-hk5&4w+%m8j3'


#########################
#                       #
#   Optional settings   #
#                       #
#########################

# Specify one or more name and email address tuples representing Base adminstrators. These people will be notify of
# applications errors (assuming correct email serrings are provided).'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL = {
    # 'TLS': False,
    # 'SERVER': '',
    # 'PORT': 25,
    # 'USERNAME': '',
    # 'TIMEOUT': 10, 
    # 'FROM_EMAIL': '',
    # 'BACKENDS' : False,
}

# Enable custom logging.
# http://docs.djangoproject.com/en/stable/topics/logging/
LOGGING = {}

# Setting this to True will only authenticate users to access any part of Base. By default anonymous users
# are permitted to access most data in Base (excluding secrets) but not make any changes.
LOGING_REQUIRED = False

# The length of time (in seconds) for which a user will remain logged into the web UI before being prompted to
# re-authentication. (Default: 1209600 [14 days])
LOGING_TIMEOUT = None

# The file path where uploaded media such as image attachments are stored. 
MEDIA_ROOT = '/opt/config/media'

# All API customer can request an arbitrary number of objects =by appending the "limit" parameter to the URL (e.g.
# "?limit=100"). This setting defines the maximun limit. Setting it to 0 or None will allow an API consumer to request
# all objects by specifying "?limit=0".
MAX_PAGE_SIZE = 1000

# The file path ere uploaded media such as image attachments are store. A trailing slash is not needed. Note that
# the default value of this settings is derived from the installed location.
# MEDIA_ROOT = '/opt/src/media'

# by default uploaded media is sotred on the local filesystem. Using Django-storages is also supported. Provide the 
# class path of the sotrage driver in STORAGE_BACKEND and an configuration options in STORAGE_CONFIG. For example:
# STORAGE_BACKEND = 'storage.backends.s3boto3Storage'
# STORAGE_CONFIG = {
#     'AWS_ACCESS_KEY_ID': 'key ID'
#     'AWS_SECRET_ACCESS_KEY: 'Secret'
#     'AWS_STORAGE_BUCKET_NAME': 'netbox'
#     'AWS_S3_REGION_NAME': 'eu-west-1'
# }

# Determine how many objects to display per page within a list (Default: 50)
PAGINATE_COUNT = 50

# By default Base will store session data in the database. Alternatively, a file path can be specified here to use
# local file storage instead. (this can be useful for enabling authentication on a standby instance with read-only
# database access.) Note that the user as which Base runs must have read and write permissions on this path.
SESSION_FILE_PATH = None

# Time zone (default: UTC)
TIME_ZONE = 'UTC'

# Date/time formatting. See the followint link for supported formats:
# http://docs.djangoproject.com/en/stable/ref/templated/builtins/#date
DATE_FORMAT = 'N j, Y'
SHORT_DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'g:i a'
SHORT_TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'N j, Y g:i a'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'
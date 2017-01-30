# # custom_storages.py
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.STATIC_BUCKET_NAME
    #https_validate_certificates = False
    secure_urls = True

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.MEDIA_BUCKET_NAME
    secure_urls = True

class SecureStorage(S3Boto3Storage):
    bucket_name = settings.SECURE_BUCKET_NAME
    querystring_auth = True
    secure_urls = True
    querystring_expire = settings.SECURE_BUCKET_EXPIRE
    default_acl = "private"

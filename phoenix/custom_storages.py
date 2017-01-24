# # custom_storages.py
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import boto3

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.STATIC_BUCKET_NAME
    #custom_domain = settings.STATIC_CUSTOM_DOMAIN
    #https_validate_certificates = False
    # querystring_auth = True
    secure_urls = True
    #calling_format = boto3.s3.connection.OrdinaryCallingFormat()
    # querystring_expire = 30000

class MediaStorage(S3Boto3Storage):
    bucket_name = settings.MEDIA_BUCKET_NAME
    #custom_domain = settings.MEDIA_CUSTOM_DOMAIN
    #calling_format = boto3.s3.connection.OrdinaryCallingFormat()
    # querystring_auth = True
    secure_urls = True
    # querystring_expire = 30000

class SecureStorage(S3Boto3Storage):
    bucket_name = settings.SECURE_BUCKET_NAME
    #calling_format = boto3.s3.connection.OrdinaryCallingFormat()
    querystring_auth = True
    secure_urls = True
    querystring_expire = settings.SECURE_BUCKET_EXPIRE
    default_acl = "private"

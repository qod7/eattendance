# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['eattendance.tk', '127.0.0.1']

# gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'attendance.passion@gmail.com'
EMAIL_HOST_PASSWORD = 'mundrekovaisi'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

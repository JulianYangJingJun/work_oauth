import pytz
import datetime
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import HTTP_HEADER_ENCODING
from django.core.cache import cache
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)


class Auth(BaseAuthentication):

    def authenticate(self, request):
        return request.session.get('userinfo'), None
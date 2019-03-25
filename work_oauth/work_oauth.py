# -*- coding: utf-8 -*-

import pytz
import datetime
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import HTTP_HEADER_ENCODING
from django.core.cache import cache
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 1)

"""Main module."""


class Permission(BasePermission):

    def has_permission(self, request, view):
        if request.session.get('userid') is not None:
            res = True
        else:
            res = False
        return res


class Auth(BaseAuthentication):

    def authenticate(self, request):
        return request.session.get('userid'), None
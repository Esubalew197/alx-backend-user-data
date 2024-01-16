#!/usr/bin/env python3
'''Authentication module
'''
from flask import request
from typing import List, TypeVar
import re


class Auth:
    '''User Authentication class
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None

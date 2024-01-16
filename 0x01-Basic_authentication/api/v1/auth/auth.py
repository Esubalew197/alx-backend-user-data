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
        '''Ensures authentication is required
        '''
        if path is not None and excluded_paths is not None:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        '''includes authorization header to http req
        '''
        if request is not None:
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Retrieves the current users
        '''
        return None

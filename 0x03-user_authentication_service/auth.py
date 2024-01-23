#!/usr/bin/env python3
'''user authentication module
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''Hashe and encrypt a password.
    '''
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

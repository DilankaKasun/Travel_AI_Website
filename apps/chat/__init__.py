# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 FutureX. All rights reserved.

"""

from flask import Blueprint

blueprint = Blueprint(
    'chat_blueprint',
    __name__,
    url_prefix=''
)

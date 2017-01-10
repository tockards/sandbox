#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tockards <tockards@tockards-ska>
#
# Distributed under terms of the MIT license.

"""
This is the celery config
"""
from os import environ

BROKER_URL = environ['BROKER_URL']
CELERY_RESULT_BACKEND = environ['BACKEND']
INCLUDE = ['daemonized.tasks']

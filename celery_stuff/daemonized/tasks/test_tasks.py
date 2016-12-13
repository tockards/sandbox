#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tockards <tockards@tockards-ska>
#
# Distributed under terms of the MIT license.

"""

"""
from daemonized.worker.celery_worker import celery



@celery.task
def hello():
    print 'hello'

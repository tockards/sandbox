#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tockards <tockards@tockards-ska>
#
# Distributed under terms of the MIT license.

"""

"""

from __future__ import absolute_import 

from celery import Celery

celery = Celery(include=[
                         'daemonized.tasks.test_tasks'
    ])

celery.config_from_object('daemonized.celeryconfig')

if __name__ == '__main__':
    celery.start()

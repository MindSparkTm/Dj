# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'library'

    def ready(self):
        import library.signals

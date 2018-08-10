# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class AjitamaConfig(ModuleMixin, AppConfig):
    name = 'ajitama'
    icon = '<i class="material-icons">extension</i>'


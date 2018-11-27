#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
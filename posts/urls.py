#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.homepageview, name='home'),
]
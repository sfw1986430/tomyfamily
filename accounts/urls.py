#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from accounts import views

urlpatterns = [
path('signup/', views.SignUpView, name='signup'),
]
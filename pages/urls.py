#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  django.urls import path
from pages import views

urlpatterns = [
    path('about/', views.about_page_view, name='about'),
    path('', views.home_page_view, name='home'),
]
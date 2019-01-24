#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from blog.models import Post



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

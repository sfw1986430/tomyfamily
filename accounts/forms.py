#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="密码",
        max_length=256,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="确认密码",
        max_length=256,
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(r"Password don't match.")
        return cd['password2']
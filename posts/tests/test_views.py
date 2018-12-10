#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.urls import reverse
from posts.models import Post

class PostModeTest(TestCase):
    def setUp(self):
        Post.objects.create(text='1 test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, '1 test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='2 test')

    def test_view_url_exists_at_prpper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/home.html')

        

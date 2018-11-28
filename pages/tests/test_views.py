#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


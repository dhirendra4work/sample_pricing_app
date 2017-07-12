# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser
from .models import School
from django.test import TestCase, RequestFactory
from django.http import Http404

from .views import school_list,school_detail

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        School.objects.create(name = "test name",pincode=100130)

    def test_list(self):
        # Create an instance of a GET request.
        request = self.factory.get('/schools/')
        request.user = AnonymousUser()

        
        response = school_list(request)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/schools/1')
        request.user = AnonymousUser()

        
        response = school_detail(request,1)
        self.assertEqual(response.status_code, 200)
    def test_school_not_found(self):
        # Create an instance of a GET request.
        request = self.factory.get('/schools/122')
        request.user = AnonymousUser()

        school_found = True
        try:
        	response = school_detail(request,122)
        except Exception as e:
        	if isinstance(e,Http404):
        		school_found = False
        	
        self.assertEqual(school_found, False)

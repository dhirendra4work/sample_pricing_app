# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import School
from .serializer import SchoolSerializer
from rest_framework.response import Response
from rest_framework import status

class SchoolViewSet(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	def create(self, request):
		return Response({"detail":"method not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def update(self, request, pk=None):
		return Response({"detail":"method not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def partial_update(self, request, pk=None):
		return Response({"detail":"method not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)

	def destroy(self, request, pk=None):
		return Response({"detail":"method not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
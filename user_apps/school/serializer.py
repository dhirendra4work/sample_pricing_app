# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):

	class Meta:
		model = School
		fields = '__all__'
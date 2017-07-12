# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class School(models.Model):

	name = models.CharField(_('school name'),max_length=75)
	pincode = models.PositiveIntegerField(_('school pincode'),validators=[MinValueValidator(100000),MaxValueValidator(999999)])

	class Meta:
		unique_together = ('name','pincode')


class BaseTable(models.Model):

	bids = models.CharField(_('Bids'),primary_key=True,max_length=20)
	base_price = models.PositiveIntegerField(_('Base Price'))

	class Meta:
		db_table = 'base_price'

class TestRRP(models.Model):
	STATUS_CHOICES = (
		('0','pending'),
		('1','approved')

	)

	bids = models.CharField(_('Bids'),max_length=20)
	rrp = models.PositiveIntegerField(_('RRP'))
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)

	class Meta:
		db_table = 'test_rrp'



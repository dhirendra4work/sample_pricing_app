# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from .models import School,TestRRP
import csv

# Create your views here.
def school_list(request):
	school_list = School.objects.all()
	context = {"school_list":school_list}
	return render(request,'school/list.html',context)

def school_detail(request,school_id):
	try:
		school_obj = School.objects.get(id=school_id)
	except School.DoesNotExist:
		raise Http404("Question does not exist")
	context = {"school":school_obj}
	return render(request,'school/detail.html',context)

def HomeView(request):
	return render(request,'school/home.html')

def ReviewView(request):

	if request.method == 'POST':
		rrp_file = request.FILES['test_rrp']
		test_rrp_list = []

		#read csv file and create list for bulk update
		with rrp_file as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				test_rrp_obj = TestRRP(bids=row['bids'],rrp=row['rrp'],status='0')
				test_rrp_list.append(test_rrp_obj)

		#bulk insert test_rrp data
		TestRRP.objects.bulk_create(test_rrp_list)

	#Get review data from db
	review_data = get_saved_bids()
	context = {"bids":review_data}
	return render(request,'school/review.html',context)

def ApprovedView(request):

	if request.method == 'POST':
		to_be_approved = request.POST.getlist('to_be_approved')
		if to_be_approved:
			TestRRP.objects.filter(id__in = to_be_approved).update(status = 1)


	#Get approved data from db
	review_data = get_saved_bids(filter = 'approved')
	context = {"bids":review_data}
	return render(request,'school/approved.html',context)
def get_saved_bids(filter=None):
	from django.db import connection
	cursor = connection.cursor()
	sql_query = "select test_rrp.bids, base_price,rrp,status,test_rrp.id from test_rrp join base_price on test_rrp.bids = base_price.bids"
	
	#fetch only approved bids if only approved bids needed
	if filter == 'approved':
		sql_query = sql_query + " where status = '1'"
	
	cursor.execute(sql_query)
	return cursor.fetchall()
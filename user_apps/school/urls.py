# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import routers
from .api_views import SchoolViewSet
from .views import school_list,school_detail,HomeView,ReviewView,ApprovedView
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'v1/schools', SchoolViewSet)
#urlpatterns = router.urls

urlpatterns = [
	url(r'^$', HomeView,name = 'upload bids'),
	url(r'^review$', ReviewView,name = 'review bids'),
	url(r'^approved$', ApprovedView,name = 'approved bids'),
    url(r'^schools/$', school_list,name = 'school list'),
    url(r'^schools/(?P<school_id>[\d]+)/$', school_detail,name = 'school detail'),
]

urlpatterns = urlpatterns + router.urls
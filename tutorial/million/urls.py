from  django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns=[
    path('Groups',views.GroupsView.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)
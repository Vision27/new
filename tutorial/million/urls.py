from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('groups', views.GroupsView.as_view()),
    path('singer', views.SingerView.as_view()),
    path('concert', views.ConcertView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
urlpatterns += [path('api-auth/', include('rest_framework.urls')),]
urlpatterns = format_suffix_patterns(urlpatterns)

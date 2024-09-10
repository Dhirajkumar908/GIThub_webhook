from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('github_webhook/',views.github_webhook,name='github_webhook'),
    path('push/',views.push, name='push'),
    path('pull_request/', views.pull_request, name='pull_request'),
    path('merge_event/', views.merge_event, name='merge_event')
]
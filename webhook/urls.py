from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('github_webhook/',views.github_webhook,name='github_webhook')
]
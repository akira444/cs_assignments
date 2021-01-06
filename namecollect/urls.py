from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'namecollect'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.PersonCreate.as_view(), name = 'person_create'),
]
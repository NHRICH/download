from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-lead/', views.submit_lead, name='submit_lead'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
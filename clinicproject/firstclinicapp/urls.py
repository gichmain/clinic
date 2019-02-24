from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('addpatient/', views.register_patient, name = 'register_patient'),
    path('search/', views.search, name = 'search'),
    path('search/patient/<int:id>/', views.PatientUpdate.as_view(), name = 'patient_details')
]


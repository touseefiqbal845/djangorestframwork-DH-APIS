from django.urls import path
from doctorhunt_app.views.doctor_frontend import doctor_list, api_doctor_detail

urlpatterns = [
    path('list/', doctor_list, name='doctor_list'),
    path('<int:doctor_id>/', api_doctor_detail, name='doctor_detail'),
]

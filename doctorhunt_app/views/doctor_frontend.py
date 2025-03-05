from django.shortcuts import render
import requests
from django.http import JsonResponse
from doctorhunt_app.models.doctor import Doctor



API_URL = "http://127.0.0.1:8000/doctors/doctors"

def doctor_list(request):
    response = requests.get(API_URL)
    doctors = response.json().get('doctors', [])
    
    return render(request, 'doctors_list.html', {'doctors': doctors})

def api_doctor_detail(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor_data = {'id': doctor.id, 'name': doctor.name}
        return render(request, 'doctor_detail.html', {'doctor': doctor_data})

    except Doctor.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)

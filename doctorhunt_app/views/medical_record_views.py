# doctorhunt_app/views/medical_record_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from doctorhunt_app.models.medical_record import MedicalRecord
from doctorhunt_app.serializers.medical_record_serializer import MedicalRecordSerializer

class MedicalRecordListCreateView(APIView):
    def get(self, request):
        records = MedicalRecord.objects.select_related("patient").all()
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalRecordDetailView(APIView):
    def get(self, request, pk):
        record = get_object_or_404(MedicalRecord.select_related('patient'), pk=pk)
        serializer = MedicalRecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        record = get_object_or_404(MedicalRecord, pk=pk)
        serializer = MedicalRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        record = get_object_or_404(MedicalRecord, pk=pk)
        record.delete()
        return Response({"message": "Medical record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

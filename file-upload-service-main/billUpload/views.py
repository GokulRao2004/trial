from django.shortcuts import render
# YourAppName/views.py

import pandas as pd
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)

        if file_serializer.is_valid():
            uploaded_file = file_serializer.validated_data['file']

            # Check if the uploaded file has a .xlsx extension
            if not uploaded_file.name.lower().endswith('.xlsx'):
                return Response({'error': 'Invalid file format. Please upload a .xlsx file.'}, status=status.HTTP_400_BAD_REQUEST)

            # Read the content of the Excel file into a variable (using pandas)
            try:
                excel_data = pd.read_excel(uploaded_file)
                print(excel_data)
            except Exception as e:
                return Response({'error': f'Error reading Excel file: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

            # You can now use 'excel_data' as a variable containing the contents of the Excel file

            # If needed, you can save the uploaded file to the database or perform other operations

            return Response({'success': 'File uploaded and processed successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

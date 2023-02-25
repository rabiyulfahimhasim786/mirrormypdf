from rest_framework import serializers
from .models import Pdf, Pdfurl

class PdfSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pdf
    fields = '__all__'

class PdfurlSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pdfurl
    fields = '__all__'
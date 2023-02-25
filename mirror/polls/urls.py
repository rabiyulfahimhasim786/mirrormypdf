from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (PdfListCreateApiView, PdfUpdateDeleteApiView, PdfurlListCreateApiView, PdfurlUpdateDeleteApiView)
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('file/', views.fileload, name='fileload'),
    path('download/', views.pdfurldownlaod, name='pdfurldownlaod'),
    #path('fileuploading/', views.uploadings, name='uploadings'),
    # path('pdfform/', views.pdf_upload, name='pdf_upload'),
    # path('pdf/', views.PdfList.as_view()),
    # path('pdf/<int:pk>/', views.PdfDetail.as_view()),
    path('pdf/', PdfListCreateApiView.as_view(), name='pdf'),
    path('pdf/<int:pk>/', PdfUpdateDeleteApiView.as_view(), name='pdf-detail'),
    path('pdfurl/', PdfurlListCreateApiView.as_view(), name='pdf'),
    path('pdfurl/<int:pk>/', PdfurlUpdateDeleteApiView.as_view(), name='pdf-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
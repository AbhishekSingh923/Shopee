from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', ProductUploadView.as_view(), name='upload-product'),
    
]
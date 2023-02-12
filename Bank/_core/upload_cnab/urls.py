from django.urls import path
from .views import store_file

urlpatterns = [
    path("cnab/", store_file, name='cnab')
]
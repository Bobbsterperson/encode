from django.urls import path
from .views import user_registration, input_text

urlpatterns = [
    path('input_text/<int:user_id>/', input_text, name='input_text'),
]

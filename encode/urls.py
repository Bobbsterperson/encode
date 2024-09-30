from django.contrib import admin
from django.urls import path, include
from app.views import user_registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_registration, name='user_registration'),
    path('app/', include('app.urls')),
]

from django.contrib import admin
from .models import User, EncodedText
admin.site.register(User)
admin.site.register(EncodedText)

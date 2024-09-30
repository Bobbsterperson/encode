from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, EncodedTextForm
from .models import User, EncodedText
import base64
import hashlib

def user_registration(request):
    user = None
    encoded_texts = []
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            encoding_type = form.cleaned_data['region']
            user, created = User.objects.get_or_create(name=name, defaults={'region': encoding_type})
            if not created:
                user.region = encoding_type
                user.save()
                encoded_texts = EncodedText.objects.filter(user=user)
            return redirect('input_text', user_id=user.id)
    else:
        form = UserForm()
    return render(request, 'app/user_registration.html', {'form': form, 'user': user, 'encoded_texts': encoded_texts})

def input_text(request, user_id):
    user = get_object_or_404(User, id=user_id)
    encoded_texts = EncodedText.objects.filter(user=user)
    if request.method == 'POST':
        text_form = EncodedTextForm(request.POST)
        if text_form.is_valid():
            original_text = text_form.cleaned_data['original_text']
            encoded_text = ''
            if user.region == 'Base64':
                encoded_text = base64.b64encode(original_text.encode()).decode()
            elif user.region == 'Hash':
                encoded_text = hashlib.sha256(original_text.encode()).hexdigest()
            EncodedText.objects.create(user=user, original_text=original_text, encoded_text=encoded_text)
            return redirect('input_text', user_id=user.id)
    else:
        text_form = EncodedTextForm()
    return render(request, 'app/input_text.html', {'form': text_form, 'user': user, 'encoded_texts': encoded_texts})
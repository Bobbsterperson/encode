import base64
from django.shortcuts import render
from .forms import InputDataForm
from .models import InputData

def stuff(request):
    form = InputDataForm()
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            form.save()
            form = InputDataForm()
    submitted_data = []
    for item in InputData.objects.all():
        original_text = item.topic
        encoded_text = base64.b64encode(original_text.encode('utf-8')).decode('utf-8')
        submitted_data.append((original_text, encoded_text))
    return render(request, 'app/input_form.html', {'form': form, 'submitted_data': submitted_data})

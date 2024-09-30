# app/views.py
from django.shortcuts import render
from .forms import InputDataForm
from .models import InputData

def stuff(request):
    form = InputDataForm()
    submitted_data = InputData.objects.all()  # Fetch all submitted data from the database

    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            form = InputDataForm()  # Reset the form after submission

    return render(request, 'app/input_form.html', {'form': form, 'submitted_data': submitted_data})

from django.shortcuts import render
from mainapp.forms import NewUserForm
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):
    return render(request, 'mainapp/home.html')

def form_fun(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Occurred")

    return render(request, 'mainapp/form.html', {'form':form})

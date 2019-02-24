from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegisterPatientForm, SearchForm
from .models import Patient
from django.views.generic.edit import UpdateView

# Create your views here.

class PatientUpdate(UpdateView):
    model = Patient
    template_name_suffix = '_patient'
    fields = ['first_name', 'last_name', 'notes']
    def get_object(self, queryset=None):
        obj = Patient.objects.get(id=self.kwargs['id'])
        return obj

@login_required(login_url = 'accounts/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url = 'accounts/login')
def register_patient(request):
    id = {} 
    form = RegisterPatientForm()
    if request.method == "GET":
        return render(request, 'patient_details.html', {'form':form})
    elif request.method == "POST":
        print("enter save phase")
        form = RegisterPatientForm(request.POST)
        patient = form.save()
        id['id']=patient.id
        print(patient.id)
        print("exit save phase")
    return render(request, 'home.html',{'id':id})

@login_required(login_url = 'accounts/login')
def search(request):
    form = SearchForm()
    if request.method == 'GET':
        return render(request, 'search.html', {'form':form})
    elif request.method == "POST":
        form = SearchForm(request.POST)
        id = request.POST.get('search_id')
        print(id)
        return redirect('patient/'+str(id))

        
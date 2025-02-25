from django.shortcuts import render
from .models import Truck, Selection, Exit, Admmission
from .forms import SelectionForm, ExitForm, AdmmissionForm
from datetime import datetime

today = datetime.today()
year=today.year; month =today.month; day=today.day

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def selection(request):
    context = {
        'form' : SelectionForm(), 
        'selected_trucks': Selection.objects.filter(date__year=year, date__month=month, date__day=day).order_by('fleet', 'officer').values()
    }
    return render(request, 'selection.html', context)

def create_selection_form(request):
    if request.method == 'POST':
        cab_no = request.POST['cab_no']
        cab_no=cab_no.upper()
        cab_no=cab_no.replace(' ', '-')

        # Try assigning an officer
        try:
            officer = Truck.objects.get(cab_no=cab_no).officer
        except:
            officer = None

        # Try assigning a fleet
        try:
            fleet = Truck.objects.get(cab_no=cab_no).fleet
        except:
            fleet = None

        form = SelectionForm(request.POST or None)
        form.officer=officer
        form.fleet=fleet
        if form.is_valid():
            selection = form.save(commit=False)
            selection.officer = officer
            selection.fleet = fleet
            selection.save()
            context = {'truck' : selection}
            return render(request, 'partials/selection_list.html', context)

    return render(request, 'partials/form.html', {'form': SelectionForm})

def exit(request):
    context = {
        'form' : ExitForm(),
        'exits': Exit.objects.filter(date__year=year, date__month=month, date__day=day).order_by('fleet', 'officer').values()
    }
    return render(request, 'exit.html', context)

def create_exit_form(request):
    if request.method == 'POST':
        cab_no = request.POST['cab_no']
        cab_no=cab_no.upper()
        cab_no=cab_no.replace(' ', '-')

        # Try assigning an officer
        try:
            officer = Truck.objects.get(cab_no=cab_no).officer
        except:
            officer = None

        # Try assigning a fleet
        try:
            fleet = Truck.objects.get(cab_no=cab_no).fleet
        except:
            fleet = None

        form = ExitForm(request.POST or None)
        form.officer=officer
        form.fleet=fleet
        if form.is_valid():
            exit = form.save(commit=False)
            exit.officer = officer
            exit.fleet = fleet
            exit.save()
            context = {'truck' : exit}
            return render(request, 'partials/exit_list.html', context)
    return render(request, 'partials/exit_form.html', {'form': ExitForm})

def admmission(request):
    context = {
        'form' : AdmmissionForm(),
        'admmissions': Admmission.objects.filter(date__year=year, date__month=month, date__day=day).order_by('fleet', 'officer').values()
    }
    return render(request, 'admmission.html', context)

def create_admmission_form(request):
    if request.method == 'POST':
        cab_no = request.POST['cab_no']
        cab_no=cab_no.upper()
        cab_no=cab_no.replace(' ', '-')

        # Try assigning an officer
        try:
            officer = Truck.objects.get(cab_no=cab_no).officer
        except:
            officer = None

        # Try assigning a fleet
        try:
            fleet = Truck.objects.get(cab_no=cab_no).fleet
        except:
            fleet = None

        form = AdmmissionForm(request.POST or None)
        form.officer=officer
        form.fleet=fleet
        if form.is_valid():
            admited = form.save(commit=False)
            admited.officer = officer
            admited.fleet = fleet
            admited.save()
            print(admited)
            context = {'truck' : admited}
            return render(request, 'partials/admmission_list.html', context)
    return render(request, 'partials/admmission_form.html', {'form': AdmmissionForm})



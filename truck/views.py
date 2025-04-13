from django.shortcuts import render, redirect
from .models import Truck, Selection, Exit, Admmission, Reservation
from .forms import SelectionForm, ExitForm, AdmmissionForm, ReservationForm, TruckForm
from datetime import datetime, timedelta
from django.contrib import messages
import csv, io
# from django.views.generic import FormView

today = datetime.today()
year=today.year; month =today.month; day=today.day

yesterday = today - timedelta(days=1)
yesterday_year=yesterday.year; yesterday_month=yesterday.month; yesterday_day=yesterday.day

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
    selected_yesterday = Selection.objects.filter(date__year=yesterday_year, date__month=yesterday_month, date__day=yesterday_day)
    admmissions = Admmission.objects.filter(date__year=year, date__month=month, date__day=day).order_by('fleet', 'officer').values()
    admmitted_cab_nos = admmissions.values_list('cab_no')
    selected_not_admitted = selected_yesterday.exclude(cab_no__in=admmitted_cab_nos).order_by('fleet', 'officer').values()
    context = {
        'form' : AdmmissionForm(),
        'admmissions': admmissions,
        'not_admited_cabs': selected_not_admitted
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

def reservation_file_form(request,):
    twks = Reservation.objects.filter(notification_date=today, type='N1').order_by('fleet', 'officer', 'cab_no').values()
    n_twks = Reservation.objects.filter(notification_date=today, type='N1').order_by('fleet', 'officer').count()
    n_cng_twks = Reservation.objects.filter(notification_date=today, type='N1', fleet='FLEET 6').order_by('fleet', 'officer').count()
    hbds = Reservation.objects.filter(notification_date=today, type='N2', ).order_by('fleet', 'officer', 'cab_no').values()
    n_hbds = Reservation.objects.filter(notification_date=today, type='N2').order_by('fleet', 'officer').count()
    n_cng_hbds = Reservation.objects.filter(notification_date=today, type='N2', fleet='FLEET 6').order_by('fleet', 'officer').count()
    context ={}
    context['twks']=twks
    context['n_twks']=n_twks
    context['n_cng_twks']=n_cng_twks
    context['hbds']=hbds
    context['n_hbds']=n_hbds
    context['n_cng_hbds']=n_cng_hbds
    context['sum']=n_hbds + n_twks
    if request.method=='POST':
        form = ReservationForm(request.POST, request.FILES)

        # VALIDATION
        if form.is_valid():
            csv_file = form.cleaned_data['data_file'].file
            if not form.cleaned_data['data_file'].name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('truck:reservation-file-form')
            if form.cleaned_data['data_file'].multiple_chunks():
                messages.error(request, 'Upload is too large (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('truck:reservation-file-form')
                
            # PROCESSING
            f = io.TextIOWrapper(csv_file)
            reader = csv.DictReader(f)
            for row in reader:
                # Try assigning an officer
                try:
                    officer = Truck.objects.get(cab_no=row['ï»¿Equipment']).officer
                except:
                    officer = None

                # Try assigning a fleet
                try:
                    fleet = Truck.objects.get(cab_no=row['ï»¿Equipment']).fleet
                except:
                    fleet = None
                

                try:
                    record = Reservation(
                        notification_date = f'{row['Notif. Date'][6:]}-{row['Notif. Date'][0:2]}-{row['Notif. Date'][3:5]}', 
                        cab_no = row['ï»¿Equipment'], 
                        notification = row['Notification'], 
                        type = row['Notifictn Type'], 
                        description = row['Description'], 
                        reported_by = row['Reported By'], 
                        officer = officer, 
                        fleet = fleet, )
                    record.save()
                except:
                    pass
                context['feedback']= 'Saved'

    else:
        form = ReservationForm()
    context['form']=form

    return render(request, 'reservation_file.html', context)


def update_trucks(request,):
    context ={}
    if request.method=='POST':
        form = TruckForm(request.POST, request.FILES)

        # VALIDATION
        if form.is_valid():
            csv_file = form.cleaned_data['data_file'].file
            if not form.cleaned_data['data_file'].name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('truck:update-trucks')
            if form.cleaned_data['data_file'].multiple_chunks():
                messages.error(request, 'Upload is too large (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('truck:update-trucks')
                
            # PROCESSING
            f = io.TextIOWrapper(csv_file)
            reader = csv.DictReader(f)
            Truck.objects.all().delete()
            for row in reader:
                try:
                    record = Truck(
                        truck_no = row['truck_no'], 
                        officer = row['officer'], 
                        cab_no = row['cab_no'], 
                        fleet = row['fleet'], 
                        )
                    record.save()
                except:
                    pass
                context['feedback']= 'Saved'

    else:
        form = TruckForm()
    context['form']=form

    return render(request, 'truck_update.html', context)


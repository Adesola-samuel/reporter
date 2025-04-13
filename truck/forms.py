from django import forms
from .models import Selection, Exit, Admmission, Reservation
import csv
import io

class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ('cab_no', 'officer', 'fleet')
        widgets = { 'cab_no':forms.TextInput(attrs={'class': 'form-control'}), }


class ExitForm(forms.ModelForm):
    class Meta:
        model = Exit
        fields = ('cab_no', 'officer', 'fleet')
        widgets = { 'cab_no':forms.TextInput(attrs={'class': 'form-control'}), }


class AdmmissionForm(forms.ModelForm):
    class Meta:
        model = Admmission
        fields = ('cab_no', 'officer', 'fleet')
        widgets = { 'cab_no':forms.TextInput(attrs={'class': 'form-control'}), }


class ReservationForm(forms.Form):
    data_file = forms.FileField(required=True)

class TruckForm(forms.Form):
    data_file = forms.FileField(required=True)

 
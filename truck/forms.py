from django import forms
from .models import Selection, Exit

class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ('cab_no', 'officer')
        widgets = { 'cab_no':forms.TextInput(attrs={'class': 'form-control'}), }


class ExitForm(forms.ModelForm):
    class Meta:
        model = Exit
        fields = ('cab_no', 'officer')
        widgets = { 'cab_no':forms.TextInput(attrs={'class': 'form-control'}), }
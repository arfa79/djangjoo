from django import forms

class TicketForm(forms.Form):
    start_location = forms.CharField(max_length=100)
    destination_location = forms.CharField(max_length=100)
    flying_date = forms.DateField()
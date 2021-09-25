from django import forms


class UserForm(forms.Form):
    date1 = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': ' form-control','type':'date',
            'placeholder': 'Дата начала'
        }))
    date2 = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': ' form-control', 'type':'date',
            'placeholder': 'Дата окончания'
        }))

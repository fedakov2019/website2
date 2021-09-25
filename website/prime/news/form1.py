from django import forms


def spisok1(a):
    class CountryForm(forms.Form):
        OPTIONS=a
        Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              choices=OPTIONS, label='КСГ список')

    return CountryForm

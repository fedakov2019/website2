from django import forms


class CountryForm(forms.Form):
    OP = []

    def __init__(self, op, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.OP = op
        self.fields['Cod']= forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=op)



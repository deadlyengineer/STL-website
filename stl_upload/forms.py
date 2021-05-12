from django import forms


class InputsForm(forms.Form):
    input1 = forms.CharField(label="Input1", max_length=100)
    input2 = forms.CharField(label="Input2", max_length=100)
    input3 = forms.CharField(label="Input3", max_length=100)

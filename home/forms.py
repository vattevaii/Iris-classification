from django import forms

class NameForm(forms.Form):
    sepal_length = forms.FloatField(label='Length of Sepal')
    sepal_width = forms.FloatField(label='Width of Sepal')
    petal_length = forms.FloatField(label='Length of Petal')
    petal_width = forms.FloatField(label='Width of Petal')


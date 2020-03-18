from django import forms


class RollForm(forms.Form):
	roll = forms.IntegerField()

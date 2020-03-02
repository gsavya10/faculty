from django import forms

class MyForm(forms.Form):
	seats = forms.IntegerField()
	course_code = forms.CharField()

class RollForm(forms.Form):
    roll=forms.IntegerField()
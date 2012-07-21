from django import forms

class MovieAddingForm(forms.Form):
	"""Form for adding a movie to the data base"""
	name = forms.CharField(max_length = 250)
	genre = forms.CharField()
	description = forms.CharField()
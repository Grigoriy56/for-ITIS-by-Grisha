from django import forms


class TextForm(forms.Form):
	name_client = forms.CharField(max_length=500)
	weight_client = forms.FloatField()
	height_client = forms.FloatField()
	age_client = forms.IntegerField()


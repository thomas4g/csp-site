from django import forms


class DataEntryForm(forms.Form):
    """docstring for DataEntryForm"""
    Class_Options =  forms.CharField(widget = forms.Textarea, required = True)
    Minimum_Hours = forms.CharField(required = True)
    Maximum_Hours = forms.CharField(required = True)
    Start_Time = forms.CharField(required = True)
    End_Time = forms.CharField(required = True)
    Required_Classes = forms.CharField(widget = forms.Textarea, required = True)

    
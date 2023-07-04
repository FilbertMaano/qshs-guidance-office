from django import forms


class IncidentReportForm(forms.Form):
    name = forms.CharField()
    from_email = forms.EmailField(required=True)
    subject = "Incident Report"
    message = forms.CharField(widget=forms.Textarea, required=True)

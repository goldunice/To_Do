from django import forms

from mainApp.models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = "__all__"

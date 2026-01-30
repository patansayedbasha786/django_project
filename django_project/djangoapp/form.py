from django import forms
from .models import student


class studentform(forms.Model.form):
    model=student

    fields=["name","age"]
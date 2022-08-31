from django.forms import ModelForm
from .models import FormData
from django.contrib.auth.models import User


class FormDataForm(ModelForm):
    class Meta:
        model = FormData
        fields = ['form_id', 'field_id', 'value', 'record_id']

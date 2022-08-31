from django.conf import settings
from django.shortcuts import render, redirect
from .models import FormField, FormRecord, FormData
from django.utils import timezone


def index_handler(request):
    table_headers = FormField.objects.all().filter(form=1)
    table_headers_names = [field.name for field in table_headers]
    all_participants = []
    for record in FormRecord.objects.all():
        one_record = FormData.objects.all().filter(record_id=record.id)
        one_participant = [field.value for field in one_record]
        all_participants.append(one_participant)

    return render(request, 'index.html', {'table_headers': table_headers_names, 'rows': all_participants})


def register_handler(request):
    if request.method == 'POST':
        new_record = FormRecord(date=timezone.now())
        new_record.save()
        for key, value in request.POST.items():

            if key != 'csrfmiddlewaretoken':
                field_id = FormField.objects.get(name=key).pk
                participant_data = FormData(record_id=new_record.pk, form_id=1, field_id=field_id, value=value)
                participant_data.save()
            else:
                pass
        return redirect("/")
    else:
        form_fields = FormField.objects.all().filter(form__id=1)
        return render(request, 'registration_form.html', {'form_fields': form_fields})




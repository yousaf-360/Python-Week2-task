from django.contrib import admin
from .models import Doctor
from .forms import DoctorCreationForm, DoctorChangeForm

class DoctorAdmin(admin.ModelAdmin):
    add_form = DoctorCreationForm
    form = DoctorChangeForm
    list_display = ['user', 'phone_number', 'specialization', 'created_at', 'updated_at']

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form'] = self.add_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

admin.site.register(Doctor, DoctorAdmin)

from django.db import models

class Appointment(models.Model):
    doctor = models.ForeignKey('users.Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.name} on {self.scheduled_at}"
    
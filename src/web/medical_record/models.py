from django.db import models

class MedicalRecord(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('users.Doctor', on_delete=models.CASCADE)
    appointment = models.ForeignKey('appointment.Appointment', on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)
    report = models.FileField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for {self.patient.name} by Dr. {self.doctor.name}"
    
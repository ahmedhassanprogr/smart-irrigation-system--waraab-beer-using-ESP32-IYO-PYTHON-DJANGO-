from django.db import models

# Create your models here.
class PumbStatus(models.Model):
    pumb_on = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pump Status: {'On' if self.status else 'Off'} at {self.updated_at}"
    
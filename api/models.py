from django.db import models

from users.models import User


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reference = models.FloatField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)


class SensorData(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    hrv = models.FloatField()
    hrvWithInvalid = models.FloatField(default=0.0)
    hr = models.IntegerField()
    ibi = models.IntegerField()
    ibiStatus = models.IntegerField(default=404)
    timestamp = models.DateTimeField(auto_now_add=True)


class PpgGreenData(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    ppg_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.ppg_value} - {self.timestamp}"

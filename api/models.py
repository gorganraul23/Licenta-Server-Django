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
    ibiOld = models.IntegerField(default=-1)
    ibi0 = models.IntegerField(null=True, blank=True)
    ibi1 = models.IntegerField(null=True, blank=True)
    ibi2 = models.IntegerField(null=True, blank=True)
    ibi3 = models.IntegerField(null=True, blank=True)
    ibiStatus0 = models.IntegerField(null=True, blank=True)
    ibiStatus1 = models.IntegerField(null=True, blank=True)
    ibiStatus2 = models.IntegerField(null=True, blank=True)
    ibiStatus3 = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.hr} - {self.hrv} - {self.hrvWithInvalid} - {self.timestamp}"


class PpgGreenData(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    ppg_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.ppg_value} - {self.timestamp}"


class PpgRedData(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    ppg_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.ppg_value} - {self.timestamp}"


class PpgIrData(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    ppg_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session} - {self.ppg_value} - {self.timestamp}"

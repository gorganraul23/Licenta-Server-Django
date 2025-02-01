from django.db import models

from api.models import Session
from users.models import User


class ExperimentData(models.Model):
    userId = models.TextField()
    sessionId = models.TextField()
    activity = models.TextField()
    questionId = models.TextField()
    userResponse = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.userId} - {self.sessionId} - {self.activity} - {self.questionId} - {self.userResponse}"


class Experiment(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class ExperimentCorrectAnswers(models.Model):
    activity = models.TextField()
    questionId = models.TextField()
    response = models.TextField()



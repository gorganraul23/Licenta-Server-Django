from django.db import models


class ExperimentData(models.Model):
    userId = models.TextField()
    sessionId = models.TextField()
    activity = models.TextField()
    questionId = models.TextField()
    userResponse = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.userId} - {self.sessionId} - {self.activity} - {self.questionId} - {self.userResponse}"

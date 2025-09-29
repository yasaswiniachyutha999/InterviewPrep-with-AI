from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models
from bson import ObjectId

class AnalysisResult(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()  # Store as percentage
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis Result for {self.user.username}: {self.score}%"

    class Meta:
        ordering = ['-created_at']

class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_description = models.TextField()
    suggestions = models.TextField()
    improved_resume = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"

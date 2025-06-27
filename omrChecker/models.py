# models.py

from django.db import models

class MyImage(models.Model):
    studentName = models.CharField(max_length=100)
    studentOmr = models.ImageField(upload_to='uploads/',default='default.png')
    answerKey = models.ImageField(upload_to='uploads/',default='default.png')
    class Meta:
        app_label = 'omrChecker'  # <-- manually specify app name

    def __str__(self):
        return self.studentName

class outputimage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='outputs/')
    class Meta:
        app_label = 'omrChecker'  # <-- manually specify app name

    def __str__(self):
        return self.title

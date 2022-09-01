from django.db import models

class Notes(models.Model):
    #CharField ~= VARCHAR
    title = models.CharField(max_length=200)
    #TextField allows variable length text to be used (without a strict limit like CharField)
    text = models.TextField()
    #When an instance is created, auto_now_add automatically populates this column with the datetime of creation
    created = models.DateTimeField(auto_now_add=True)

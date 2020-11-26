from django.db import models


# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)


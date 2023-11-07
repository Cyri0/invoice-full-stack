from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    statuses = [
        (0,'Draft'),
        (1,'Pending'),
        (2,'Paid')
    ]

    status = models.IntegerField(choices = statuses, default=0)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_in_huf = models.IntegerField()

    def __str__(self):
        return f"{self.date} - status: {self.status}"

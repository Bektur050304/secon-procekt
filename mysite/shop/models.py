from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
            return self.title

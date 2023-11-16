from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name    
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.email
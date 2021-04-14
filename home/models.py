from django.db import models

# Create your models here.
# makemigrations - create changes and store in a file 
# migrare


class Contact(models.Model):
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    # date = models.DateField()
    
    def __str__(self):
        return self.email
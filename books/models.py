from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class ReadingSession(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    pages_read = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.book.title}"

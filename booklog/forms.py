# booklog/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Replace 'other_fields' with actual fields from your model

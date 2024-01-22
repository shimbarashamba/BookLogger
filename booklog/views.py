from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, ReadingSession
from .forms import BookForm
from django.http import HttpResponseForbidden


@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'booklog/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    sessions = ReadingSession.objects.filter(book=book)
    return render(request, 'booklog/book_detail.html', {'book': book, 'sessions': sessions})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Set the user to the current user
            book.save()
            return redirect('book_list')  # Redirect to the list of books after adding
    else:
        form = BookForm()

    return render(request, 'booklog/add_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)  # Ensure the book belongs to the current user
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books after deletion
    
    return HttpResponseForbidden()  # Return forbidden response if not POST request
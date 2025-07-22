from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse # Import JsonResponse
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(request, 'Error creating book. Please check your input.')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(request, 'Error updating book. Please check your input.')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request
            book.delete()
            messages.success(request, 'Book deleted successfully!')
            return JsonResponse({'status': 'success', 'message': 'Book deleted successfully.'})
        else:
            # Fallback for non-AJAX requests (though current setup won't hit this)
            book.delete()
            messages.success(request, 'Book deleted successfully!')
            return redirect('book_list')
    # For GET requests to /books/<pk>/delete/, show the confirmation page
    return render(request, 'books/book_confirm_delete.html', {'book': book})
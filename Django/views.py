from django.shortcuts import render, redirect

# Create your views here.
from Django.form.formBook import Book
from Django.models import Books


def index(request):
    return render(request, 'index.html')


# book
def book(request):
    books = Books.objects.all()
    return render(request, 'book.html', {'books': books})


def formBook(request, id=0):
    if request.method == "GET":
        # Hiện form add
        if id == 0:
            form = Book()
        # Hiện form update
        else:
            book = Books.objects.get(pk=id)
            form = Book(instance=book)
        return render(request, "formBook.html", {'form': form})
    else:
        # Btn add
        if id == 0:
            form = Book(request.POST)
        # Btn Update
        else:
            book = Books.objects.get(pk=id)
            form = Book(request.POST, instance=book)
        # Update valid form
        if form.is_valid():
            form.save()
        return redirect('/book')


def deleteBook(request, id):
    book = Books.objects.get(pk=id)
    book.delete()
    return redirect('/book')

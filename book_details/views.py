from django.shortcuts import render, redirect
from .models import Book
# Create your views here.


def index(request):
    return render(request, 'home.html')


def viewlist(request):
    book = Book.objects.all()
    context = {
        'books': book
    }

    return render(request, 'view_book.html', context)


def search(request):
    return render(request, 'search.html')


def addBook(request):
    if request.method == "POST":

        book_name = request.POST.get('book_name')
        publisher_name = request.POST.get('publisher_name')
        publisher_age = request.POST.get('publisher_age')
        page_no = request.POST.get('page_no')
        publication_date = request.POST.get('publication_date')
        genre = request.POST.get('genre')
        book = Book(title=book_name, publisher_name=publisher_name,
                    publisher_age=publisher_age,
                    page_no=page_no,
                    publication_date=publication_date,
                    genre=genre
                    )
        book.save()
        return redirect('view')
    return render(request, 'home.html')


def edit(request, pk):
    if request.method == "GET":
        book = Book.objects.get(serial_number=pk)
        context = {
                "book": book
                }
        return render(request, 'edit_book.html', context)
    elif request.method == "POST":
        book = Book.objects.get(serial_number=pk)
        book.title = request.POST.get("book_name")
        book.publisher_name = request.POST.get("publisher_name")
        book.publisher_age = request.POST.get("publisher_age")
        book.page_no = request.POST.get("page_no")
        book.publication_date = request.POST.get("publication_date")
        book.genre = request.POST.get("genre")
        book.save()
        return redirect('view')


def delete(request, pk):
    book = Book.objects.get(serial_number=pk)
    context = {
        'book': book
    }
    if request.method == "POST":
        book = Book.objects.get(serial_number=pk)
        book.delete()
        return redirect('view')
    return render(request, 'delete.html', context)


def search(request):
    return render(request, 'search_book.html')
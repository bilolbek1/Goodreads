from django.contrib import admin
from book.models import Book, BookReview, Author, AuthorBook


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn']
    search_fields = ['title', 'isbn']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']



class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book']
    search_fields = ['start_given']



class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ['author', 'book']
    search_fields = ['author', 'book']



admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorBook, AuthorBookAdmin)
















































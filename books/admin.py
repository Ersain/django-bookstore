from django.contrib import admin
from books.models import Book, Review


class ReviewAdmin(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewAdmin, ]
    list_display = ('title', 'author', 'price')


admin.site.register(Book, BookAdmin)

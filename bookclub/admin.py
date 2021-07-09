from django.contrib import admin
from .models import Book, Discussion

# admin.site.register(Book)
admin.site.register(Discussion)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book', 'read_by')
    ordering = ('-read_by',)
    search_fields = ['book']
    fields = (('book', 'read_by'), 'description')

from django.contrib import admin
from library import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    ...
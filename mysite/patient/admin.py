from sqlite3 import Date
from django.contrib import admin
from patient.models import Weight

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Weight, AuthorAdmin)

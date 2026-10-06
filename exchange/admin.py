from django.contrib import admin
from .models import ExchangeProgram


class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university', 'country', 'languages', 'seats', 'deadline')


admin.site.register(ExchangeProgram, ExchangeProgramAdmin)
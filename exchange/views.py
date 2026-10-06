from datetime import date

from django.shortcuts import render
from .models import ExchangeProgram


def exchange_list(request):
    today = date.today()
    all_programs = ExchangeProgram.objects.order_by('deadline')
    country = request.GET.get('country', '')

    programs = all_programs.filter(country=country) if country else all_programs
    programs = list(programs)
    for program in programs:
        program.is_open = program.deadline >= today

    countries = sorted({p.country for p in all_programs if p.country})
    return render(request, 'exchange/exchange_list.html',
                  {'programs': programs, 'countries': countries, 'selected': country})
from django.http import HttpResponse
from django.shortcuts import render
from .models import HomePage, Department, Program, Teacher


def index(request):
    page = HomePage.objects.first()
    return render(request, 'faculty/index.html', {'page': page})


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'faculty/program_list.html', {'programs': programs})


def program_detail(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
    except Program.DoesNotExist:
        return HttpResponse('Спеціальність не знайдена', status=404)
    subjects = program.course_list.all()
    return render(request, 'faculty/program_detail.html',
                  {'program': program, 'subjects': subjects})


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'faculty/department_list.html', {'departments': departments})


def department_detail(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return HttpResponse('Кафедру не знайдено', status=404)
    context = {
        'department': department,
        'programs': Program.objects.filter(release_department=department),
        'teachers': Teacher.objects.filter(home_department=department),
    }
    return render(request, 'faculty/department_detail.html', context)
from django.contrib import admin
from .models import HomePage, Department, Course, Program, Teacher


class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomePage.objects.exists()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_professor')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'about', 'coordinator', 'contact', 'release_department', 'get_courses')
    search_fields = ('name', 'code')

    def get_courses(self, obj):
        return ", ".join(course.name for course in obj.course_list.all())


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'degree', 'home_department')
    list_filter = ('home_department',)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Teacher, TeacherAdmin)



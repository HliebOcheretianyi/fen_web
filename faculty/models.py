from django.db import models


class HomePage(models.Model):
    faculty_name = models.CharField(max_length=67)
    about = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.faculty_name


class Department(models.Model):
    name = models.CharField(max_length=67)
    head_professor = models.CharField(max_length=67)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=67)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=67)
    code = models.CharField(max_length=20)
    about = models.TextField()
    coordinator = models.CharField(max_length=67)
    contact = models.CharField(max_length=20)
    release_department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='programs'
    )
    course_list = models.ManyToManyField(
        Course,
        related_name='programs',
        blank=True
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=67)
    role = models.CharField(max_length=67)
    degree = models.CharField(max_length=67, blank=True)
    home_department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers'
    )
    courses = models.ManyToManyField(
        Course,
        related_name='teachers',
        blank=True
    )

    def __str__(self):
        return self.name
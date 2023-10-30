from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    course = models.PositiveSmallIntegerField()
    student_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    detail = models.TextField(null=True, blank=True)
    isDone = models.BooleanField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.shortcuts import render, redirect
from .models import *

from .forms import *


def students(request):
    content = {
        "students": Student.objects.all()
    }
    return render(request, 'students.html', content)


def elder_students(request):
    content = {
        "elder_students": Student.objects.filter(age__gt=20)
    }
    return render(request, 'elder_students.html', content)


def student_plans(request, num):
    content = {
        "student_pans": Plan.objects.filter(id=num)
    }
    return render(request, 'student_plans.html', content)


def graduated_students(request):
    content = {
        "g_s": Student.objects.filter(course__gte=3)
    }
    return render(request, 'graduated_students.html', content)


def plans(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/plans/")
    content = {
        "plans": Plan.objects.all(),
        "plan_form": PlanForm()
    }

    return render(request, 'plans.html', content)


def graduated_student_plans(request):
    content = {
        "g_s_p": Plan.objects.filter(student_id__course=4),
        "student": Student.objects.all()
    }
    return render(request, 'graduated_student_plans.html', content)


def delete_plan(request, num):
    Plan.objects.get(id=num).delete()
    return redirect("/plans/")


def not_yet_plan(request):
    content = {
        "not_yet_plan": Plan.objects.filter(isDone=False)
    }
    return render(request, 'not_yet_plan.html', content)

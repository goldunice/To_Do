from django.contrib import admin
from django.urls import path
from mainApp.views import students, plans, not_yet_plan, graduated_students, delete_plan, elder_students, \
    graduated_student_plans, student_plans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', students),
    path('elder_students/', elder_students),
    path('graduated_students/', graduated_students),
    path('student_plans/<int:num>/', student_plans),
    path('plans/', plans),
    path('graduated_student_plans/', graduated_student_plans),
    path('delete_plan/<int:num>/', delete_plan),
    path('not_yet_plan/', not_yet_plan),

]

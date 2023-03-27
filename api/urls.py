from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("user/signUp", views.signUp, name='signUp'),
    path("user/signIn", views.signIn.as_view(), name='signIn'),
    path("user/update", views.userUpdate.as_view(), name='userUpdate'),

    path("vacancy/create", views.createVacancy, name='createVacancy'),
    path("vacancies/", views.getAllVacancies.as_view(), name='getAllVacancies'),
    path("vacancy/update/{id}", views.vacancyUpdate.as_view(), name='vacancyUpdate'),
    path("vacancy/delete/{id}", views.vacancyDelete.as_view(), name='vacancyDelete'),
]

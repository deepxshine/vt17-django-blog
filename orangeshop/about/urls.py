from django.urls import path

from .views import about_us, about_developers

app_name = 'about'

urlpatterns = [
    path('us/', about_us, name='about_us'),
    path('developers/', about_developers, name='about_developers'),

]

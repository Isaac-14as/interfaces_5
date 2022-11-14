from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('change/<int:pk>', views.change, name='change'),
    path('api', views.PhoneViews.as_view()),
    path('api/<int:id>', views.PhonesIdView.as_view()),
]




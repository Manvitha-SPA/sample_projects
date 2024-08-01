from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_url, name = "index"),
    path("data/", views.restaurantinfo, name = 'get'),
    path("ind/",views.my_form,name='my_form'),
    path("add_to_db/", views.add_to_db, name='add_to_db'),
   # path("success/",views.success_page,name="success_page"),

]
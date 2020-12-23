from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="wiki"),
    path("search/", views.search_page, name="search"),
    path("create/", views.new_page, name="create"),
    path("save/", views.save_page, name="save"),
    path("random/", views.random_page, name="random"),
    path("<str:title>/", views.get_page, name="title"),
    path("<str:title>/edit", views.edit_page, name="edit"),
    
]

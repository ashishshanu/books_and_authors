from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_all_books),
    path('authors', views.list_authors),
    path('new/author', views.register_author),
    path('new/book', views.regiter_book)
]
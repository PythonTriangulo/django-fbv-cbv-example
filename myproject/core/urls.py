from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.Index.as_view(), name='index'),
    path('home/', v.home, name='home'),
    path('book/', v.BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', v.book_detail, name='book_detail'),
    path('book/book/<int:pk>/', v.BookDetail.as_view(), name='book_detail'),
    path('book/add/', v.book_add, name='book_add'),
    path('book/book/add/', v.BookCreate.as_view(), name='book_add'),
]

from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('book/<int:pk>/', v.book_detail, name='book_detail'),
]

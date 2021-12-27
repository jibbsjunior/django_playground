from django.urls import path
# from django.urls.resolvers import URLPattern
from first_app import views
# from hello_world.first_app.views import books

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<age>/', views.show_age, name='show_age'),
    path('odd/<int:odd_or_even>/', views.even_or_odd, name='odd_or_even'),
    path('books/book', views.books, name='books')
]
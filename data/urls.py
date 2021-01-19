from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.Categories.as_view(), name='categories'),
    path('category/<int:id>', views.Category.as_view(), name='category')
]

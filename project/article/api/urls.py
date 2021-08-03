from django.urls import path
from article.api import views as api_views

urlpatterns = [
    path('texts/',api_views.text_list_create_api_view,name='text-list'),
    path('texts-detail/<int:pk>',api_views.text_detail,name='text-detail'),
]

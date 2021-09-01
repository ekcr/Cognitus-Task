from article import views
from django.urls import path
from article.api import views as api_views

urlpatterns = [
    path('texts/',api_views.apiView.as_view(),name='text-list'),
    path('texts/<int:pk>',api_views.apiView.as_view(),name='text-list'),
    path('texts/',api_views.apiViewRequest.as_view(),name='text-list'),

    
    # path('texts-detail/<int:pk>',api_views.apiViewDetail.as_view(),name='text-detail'),
]

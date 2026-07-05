from django.urls import path
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.posts_list, name='list'),
    path('<slug:slug>/', views.post_page, name='page')
    ,path('id/<int:pk>/', views.post_page_by_pk, name='page_by_pk')
]
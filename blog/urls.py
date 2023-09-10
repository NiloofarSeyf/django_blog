from django.urls import path
# from .views import post_list_view, post_detail_view, post_create_view, post_update_view, post_delete_view
from . import views

urlpatterns = [

    path('', views.PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
    # path('about', aboutview, name= 'about')
]

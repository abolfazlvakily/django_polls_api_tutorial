from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.PostListAPIView.as_view() , name = 'Post_List'),
    path('<int:id>', views.PostDetailAPIView.as_view() , name = 'Post_Detail'),
    path('<int:id>/destroy', views.PostDestroyAPIView.as_view() , name = 'Post_destroy'),
    path('<int:id>/edit', views.PostupdAPIView.as_view() , name = 'Post_upd'),
    path('create/', views.PostCreateAPIView.as_view() , name = 'Post_create_api'),
    path('img/', views.upd_img.as_view(({'get': 'list'})) , name = 'Post_img_api'),
]
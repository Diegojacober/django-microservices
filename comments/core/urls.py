from django.urls import path
from .views import CommentsApiView, PostCommentAPIView

urlpatterns = [
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view()),
    path('comments', CommentsApiView.as_view())
]
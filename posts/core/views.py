from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
import requests


class PostApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response([self.formatPost(p) for p in posts])


    def formatPost(self, post):
        comments = requests.get(f'http://127.0.0.1:8001/api/posts/{post.id}/comments').json()

        return {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments': comments
        }
        
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
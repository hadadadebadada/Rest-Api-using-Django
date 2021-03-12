from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer
from .forms import PostForm


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, '/index.html', tmpl_vars)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing article instances.
        """

    serializer_class = PostSerializer
    queryset = Post.objects.all()

from django.db.models import Q
from django.http import HttpResponse
from ..models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer

# Third Party
from rest_framework import generics, mixins

class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView): #DetailView, CreateView or FormView
    lookup_field = 'pk' #slug or id # url(r'?P<pk>\d+')
    serializer_class = PostSerializer
    #queryset = Post.objects.all()

    def get_queryset(self):        
        qt = self.request.GET.get("whoami")
        qs = ""
        if qt == "amowner":
            qs = Post.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(source__icontains=query)
                |Q(title__icontains=query)
                |Q(content__icontains=query)
                |Q(author__icontains=query)
                ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PostRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView, CreateView or FormView
    lookup_field = 'pk' #slug or id # url(r'?P<pk>\d+')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

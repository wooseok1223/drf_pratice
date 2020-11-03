from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer
from .models import Post

#
# class PublicPostListApiView(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer
#
# class PublicPostListApiView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
# public_post_list = PublicPostListApiView.as_view()


# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [IsAuthenticated]  # 인증이 되어있음을 보장 받을 수 있음
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]  # 인증이 되어있음을 보장 받을 수 있음

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']
    ordering_id = ['id']

    def perform_create(self, serializer):
        # FIXED : 인이 되어있다는 가정하에
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(ip=ip, author=author)

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = PostSerializer(post)
        return Response({
            'post' : serializer.data
        })

# def post_list(requset):
#     pass
#
#
# post_list = csrf_exempt(post_list())
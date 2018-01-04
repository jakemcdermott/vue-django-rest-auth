from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .permissions import (
    AdminOrAuthorCanEdit,
)
from .models import (
    User,
    Post,
)
from .serializers import (
    UserSerializer,
    PostSerializer,
)

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        IsAuthenticated,
    )

    @detail_route(methods=['get'])
    def posts(self, request, pk=None):
        queryset = Post.objects.filter(author__pk=pk).order_by('-created')

        context = {'request': request}

        serializer = PostSerializer(queryset, context=context, many=True)

        return Response(serializer.data)


class PostViewSet(ModelViewSet):

    queryset = Post.objects.order_by('-created')
    serializer_class = PostSerializer

    permission_classes = (
        IsAuthenticated,
        AdminOrAuthorCanEdit,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super(PostViewSet, self).perform_create(serializer)

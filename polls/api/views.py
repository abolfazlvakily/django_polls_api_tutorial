from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerCanManageOrReadOnly
from polls.models import Question, Uplooaded_images
from django.db.models import Q
from .serializer import (PostListSerializer,
                         PostDetailSerializer,
                         PostDestroySerializer,
                         PostupdSerializer,
                         PostCreateSerializer,
                         upd_img,
                         )


class PostListAPIView(generics.ListAPIView):
    # queryset = Question.objects.all()
    serializer_class = PostListSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('question_text', 'owner',)
    search_fields = ('question_text', 'owner__username',)
    ordering_fields = ('id', 'pub_date',)

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            # superuser can see all posts
            queryset = Question.objects.all()
        elif not self.request.user.is_anonymous:
            # otherwise every user can see his posts
            queryset = Question.objects.filter(owner=self.request.user)
        else:
            queryset = Question.objects.none()

        # Custom search. It is not related to rest_framework
        query = self.request.GET.get('q')
        if query:
            # if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(question_text__icontains=query) |
                Q(owner__first_name__icontains=query) |
                Q(owner__last_name__icontains=query) |
                Q(owner__username__icontains=query)
            ).distinct().order_by('-pub_date')
        return queryset


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'  # id is urls


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = PostDestroySerializer
    lookup_field = 'id'


class PostupdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = PostupdSerializer
    lookup_field = 'id'
    permission_classes = [OwnerCanManageOrReadOnly, ]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, ]


class upd_img(viewsets.ModelViewSet):
    queryset = Uplooaded_images.objects.all()
    serializer_class = upd_img

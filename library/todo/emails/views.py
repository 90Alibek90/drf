from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Article
from rest_framework.response import Response
from rest_framework.decorators importapi_view, renderer_classes
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import mixins

# Create your views here.
from .serializers import AbstractUser, User
from .models import Email
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .filters import ArticleFilter
from rest_framework.pagination import LimitOffsetPagination

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit =2

class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleLimitOffsetPagination

class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter

class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()

    def get_queryset(self):
        return Article.objects.filter(name__contains='python')

class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Article.objects.filter(name__contains=name)

class ArticleParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        return articles

class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    @action(detail=True, methods=['get'])
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.text': article.text})
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ArticleSerializer

class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    returnResponse(serializer.data)

class ArticleRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'user']

class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        returnResponse(serializer.data)

class UserModelSerializer:
    pass


class UserModelViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = UserModelSerializer


"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emails import views


from emails.views import EmailModelViewSet
from rest_framework.generics import DestroyAPIView
from rest_framework.genericsimportUpdateAPIView

router = DefaultRouter()
router.register('base', views.ArticleViewSet, basename='article')
filter_router = DefaultRouter()
filter_router.register('param', views.ArticleParamFilterViewSet)

class ArticleUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

urlpatterns = [
    path('filters/', include(filter_router.urls)),
    path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),
    path('viewsets/', include(router.urls)),
    path('generic/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('views/api-view/', views.ArticleAPIVIew.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]


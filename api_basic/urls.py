from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, ArticleListGenericAPIView, ArticleDetailGenericAPIView

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', ArticleListGenericAPIView.as_view()),
    path('generic/detail/<int:id>/', ArticleDetailGenericAPIView.as_view())
]
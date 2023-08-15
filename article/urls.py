
from django.urls import path,include
from .views import home,ArticleList,ArticleDetail

app_name="article"

urlpatterns = [
    
    path('',home,name="home"),
    path('article/',ArticleList.as_view(),name="Article"),
    path('<int:pk>/', ArticleDetail.as_view(), name='detail'),
]

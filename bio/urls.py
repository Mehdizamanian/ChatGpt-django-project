
from django.urls import path,include
from .views import bio
# home,ArticleList,ArticleDetail

app_name="bio"

urlpatterns = [
    
    path('',bio,name="biohome"),

]

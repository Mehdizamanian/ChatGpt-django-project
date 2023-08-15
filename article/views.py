from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Article
import openai


def home (request):
    # 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
    # check submission
    if request.method == "POST" :
        question = request.POST['question']
        # import ai
        # do ai stuff
        # set ai key
        openai.api_key="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"
        # create openai instance 
        openai.Model.list()
        # make a completation from by response
        response = openai.Completion.create(

            model="text-davinci-003",
            prompt=question,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # parse the response
        response = (response["choices"][0][text]).strip()
        return render(request,"article/index.html",{"question":question})

    return render(request,"article/index.html",{})



class ArticleList(ListView):
    queryset=Article.objects.all()
    template_name="article/article_list.html"

class ArticleDetail(DetailView):
    queryset=Article.objects.all()
    template_name="article/article_detail.html"




# Create your views here.

from django.shortcuts import render ,HttpResponse
from .models import Home,About,Resume,Contact,Social



def bio(request):
    homemodel=Home.objects.filter(status=True)
    aboutmodel=About.objects.filter(status=True)
    resumemodel=Resume.objects.filter(status=True)
    contactmodel=Contact.objects.filter(status=True)
    socialmodel=Social.objects.filter(status=True)
    return render(request,"bio/bio_list.html",{
        "home":homemodel,
        "about":aboutmodel,
        "resume":resumemodel,
        "contact":contactmodel,
        "social":socialmodel,
        })


# Create your views here.

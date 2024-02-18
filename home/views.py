from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):

    people =[
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 15},
        {'name': 'sanskriti', 'age': 20},
        {'name': 'pragyan', 'age': 16},
        {'name': 'seema', 'age':48},
 ]

    # return HttpResponse("hey i am a django server")
    return render(request,"home/index.html" ,context={"page":"index","people" :people})

def contact(request):
    context={"page":"contact"}
    return render(request,"home/contact.html",context)

def about(request):
    context={'page':"about"}

    return render(request,"home/about.html",context)



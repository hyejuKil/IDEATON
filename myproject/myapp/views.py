from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def chat_search(request):
    return render(request,'chat_search.html')

def hreview(request):
    return render(request,'hospital_review.html')

def mreview(request):
    return render(request,'medicine_review.html')
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def index(request):
    return render(request,'myapp/index.html')

def index_json(request):
    return render(request,'myapp/indexjson.html')
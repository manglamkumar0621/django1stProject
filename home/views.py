from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("This is homepage")
    context = {
        'variable1': 'This is sent variable string...',
        'variable2': 'Manglam'}
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")
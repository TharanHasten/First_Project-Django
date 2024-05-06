from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def htmlPage(request):
    return render(request, 'page_1.html')
def pageRes(request):
    print(request.GET)
    print(request.GET.get('name'))
    return HttpResponse("Hello ," + request.GET.get('name'))


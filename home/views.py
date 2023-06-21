from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index-3.html')


def test(request):
    return render(request, 'home/index-test.html')


def about(request):
    return render(request, 'about/about.html')


def product(request):
    return render(request, 'product/product.html')

def business(request):
    return render(request, 'business/business.html')

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def items(request):
    return render(request, 'mainapp/items.html')


def departaments(request):
    return render(request, 'mainapp/departaments.html')


def item_types(request):
    return render(request, 'mainapp/item_types.html')

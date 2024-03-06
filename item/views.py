from django.shortcuts import render, get_object_or_404

from .models import Item

# Create your views here.

def items(request):
    # Your view logic for the 'items' page goes here
    return render(request, 'item/items.html')



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item': item
    })
    
def new(request):
    # Your view logic for the 'new' page goes here
    return render(request, 'item/new.html')

def delete(request, pk):

    return render(request, 'item/new.html')

def edit(request, pk):

    return render(request, 'item/form.html')
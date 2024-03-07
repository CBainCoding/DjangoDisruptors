from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Item

# Create your views here.

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)


    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))


    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


    


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
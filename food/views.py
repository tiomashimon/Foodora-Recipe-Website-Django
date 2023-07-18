from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.shortcuts import render
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator


def food(request):
    food_obj = Item.objects.all()
    paginator = Paginator(food_obj, 12)
    page = request.GET.get('page')

    food_request_text = request.GET.get('food_name')
    sorted_food_obj = []

    if food_request_text:
        for item in food_obj:
            if food_request_text in item.name:
                sorted_food_obj.append(item)
        paginator_for_search = Paginator(sorted_food_obj, 12)
        sorted_food_obj = paginator_for_search.get_page(page)
        return render(request, 'food/index.html', {'food': sorted_food_obj, 'food_request_text': food_request_text})

    food_obj = paginator.get_page(page)
    contex = {"food": food_obj, }

    return render(request, 'food/index.html', contex)


class FoodClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'food'


def detail(request, item_id):
    context = {}
    try:
        item = Item.objects.get(pk=item_id)
        item.clicked += 1
        item.save()
        context['item'] = item
    except Exception:
        return HttpResponse("Page is not found")
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


@login_required
def create_item(request):
    if request.user.is_authenticated:
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('food')
        return render(request, 'food/create-item.html', {'form': form})
    else:
        return redirect('login')


@login_required
def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'food/create-item.html', {'form': form, 'item': item})


@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food')

    return render(request, 'food/delete-item.html', {'item': item})


def rating(request):
    food_obj = Item.objects.all()
    for item in food_obj:
        item.clicked //= 2  # Деление рейтинга на два
    context = {"food": food_obj}
    return render(request, 'food/rating.html', context)


def home(request):
    num_of_items = len(Item.objects.all())
    return render(request, 'food/home.html', {'num_of_items': num_of_items})

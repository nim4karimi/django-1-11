from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from .models import RestaurantLocation

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'


class FastRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='FastFood')
    template_name = 'restaurants/restaurants_list.html'


class PizzaRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='Pizza')
    template_name = 'restaurants/restaurants_list.html'

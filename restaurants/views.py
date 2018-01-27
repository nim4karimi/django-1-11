from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from django.views import View
from .models import RestaurantLocation

# def restaurant_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, template_name, context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'


class SearchRestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        print(self.kwargs)
        queryset = RestaurantLocation.objects.filter(category__iexact='pizza')
        return queryset

from django.db.models import Q
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.views import View
from django.views.generic import TemplateView , ListView , DetailView
from .forms import RestaurantCreatForm
from .models import RestaurantLocation



def restaurant_createview(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        category = request.POST.get("category")
        obj = RestaurantLocation.objects.create(
            name = title,
            location = location,
            category = category
        )
        return HttpResponseRedirect("/restaurants/")
    template_name = 'restaurants/form.html'
    context = {}
    return render(request, template_name , context)
#
#
# def restaurant_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, template_name, context)
#
#

class RestaurantListView(ListView):
    def get_queryset(self):
        # print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset



class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, **kwargs):
    #     #print(self.kwargs)
    #     context = super(RestaurantDetailView,self).get_context_data(**kwargs)
    #     print(context)
    #     return context
    #
    # def get_object(self):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj= get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj
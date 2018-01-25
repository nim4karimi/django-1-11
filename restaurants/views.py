import random

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        print(context)
        num = random.randint(0, 2000000)
        some_list = [num, random.randint(0, 2000000), num]
        context = {
            'bool_var': True,
            'num': num,
            'some_list': some_list,
        }
        return context

class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
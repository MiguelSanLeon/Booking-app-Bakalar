from django.shortcuts import render
from django.views import generic, View
from .models import Booking


# Create your views here.

class HomePage(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

from django.shortcuts import render
from .models import Greeting

# Create your views here.
def greeting_view(request):
    greeting = Greeting.objects.last()
    return render(request, 'greeting/greeting.html',
                  {
                      'greeting': greeting
                  })

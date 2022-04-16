from django.http import HttpResponse


# Create your views here.
def greeting_view(request):
    return HttpResponse("Hello!")

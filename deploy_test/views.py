from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Hasna, this is your first deploy.")

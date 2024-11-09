from django.http import HttpResponse

def categoria_list(request):
    return HttpResponse("Categorías disponibles")
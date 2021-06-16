from django.shortcuts import render
from .models import New
from hitcount.views import HitCountDetailView

class count(HitCountDetailView):
    count_hit = True

def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = New.objects.filter(title__icontains=search_query)
    else:
        news = New.objects.order_by("-pk")[:8]

    return render(request, 'news/index.html', {'title': 'NEONews', 'news': news})


def about(request):
    return render(request, 'news/about.html')


def contact(request):
    return render(request, 'news/contact.html')
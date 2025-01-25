from django.shortcuts import render
from .models import NewCategory, News

# Create your views here.


def home_page(request):

    category = NewCategory.objects.all()
    news = News.objects.all()
    context = {'category': category , 'news':news}

    return render(request, 'home.html', context)

def category_page(request, pk):

    category = NewCategory.objects.get(id=pk)

    news = News.objects.filter(news_category=category)

    context = {'category': category, 'news': news}

    return render(request, 'category.html', context)


def news_page(request, pk):

    news = News.objects.get(id=pk)

    context = {'news': news}

    return render(request, 'news.html', context)






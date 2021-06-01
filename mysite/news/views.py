from django.shortcuts import render, redirect
from .models import Art
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from urllib.request import urlopen


def news_home(req):
    # news = Art.objects.all()
    news = Art.objects.order_by('vtime')  # или минус или -date [:-1]
    return render(req, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Art
    template_name = 'news/details_view.html'
    context_object_name = 'artic'

class NewsDeleteView(DeleteView):
    model = Art
    template_name = 'news/news-delete.html'
    success_url = '/news/'


class NewsUpdateView(UpdateView):
    model = Art
    template_name = 'news/create.html'

    form_class = ArticlesForm

def success(req):


    #url = "https://sms.ru/sms/send?api_id=B36C6249-C30C-3209-E2D9-3DB899EBC2FF&to=79500203481,74993221627&msg=uspeshno+zabronirovan&json=1"
   # urlopen(url)

    return render(req, 'news/success.html')

def create(req):
    error = ''
    if req.method == 'POST':
        form = ArticlesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            error = 'Форма неправильная'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(req, 'news/create.html', data)

def createhost(req):
    error = ''
    if req.method == 'POST':
        form = ArticlesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма неправильная'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(req, 'news/createH.html', data)
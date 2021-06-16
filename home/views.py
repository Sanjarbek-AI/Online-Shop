from django.db.models import Q
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from home.forms import ContactModelForm
from home.models import ContactModel, NewsModel


class HomeTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_news'] = NewsModel.objects.order_by('-pk')[0:8]
        return context


class ContactCreateView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('home:contact')


class NewsListView(ListView):
    template_name = 'layouts/news.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return NewsModel.objects.filter(
            Q(title__icontains=q) |
            Q(short_description__icontains=q)
        )


class NewsDetailView(DetailView):
    template_name = 'news-detail.html'
    model = NewsModel

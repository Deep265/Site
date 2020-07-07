from django.shortcuts import render
from .models import Profile
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DeleteView,UpdateView,ListView,DetailView
# Create your views here.
class LinkList(ListView):
    model = Profile

class LinkDetail(DetailView):
    model = Profile

class LinkUpdate(UpdateView):
    model = Profile

class LinkDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('site_links:all')

class LinkCreate(CreateView):
    model = Profile
    fields = ('name','link','img','description','img_link')
    success_url = reverse_lazy('site_links:all')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.user.save()
        return super().form_valid(form)

class LinkUpdateView(UpdateView):
    model = Profile
    fields = ('name','link','img','description','img_link')
    success_url = reverse_lazy('site_links:all')


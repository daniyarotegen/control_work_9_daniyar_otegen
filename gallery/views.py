from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gallery.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo_list.html'
    ordering = ['-created_at']


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo_form.html'
    fields = ['image', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo_form.html'
    fields = ['image', 'caption']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo_confirm_delete.html'
    success_url = reverse_lazy('photo_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)


class AddFavoriteView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = []

    def form_valid(self, form):
        photo = form.instance
        photo.favorite_users.add(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('photo_detail', kwargs={'pk': self.kwargs['pk']})




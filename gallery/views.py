from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gallery.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'home.html'
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

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    template_name = 'photo_form.html'
    fields = ['image', 'caption']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect('photo_detail', kwargs={'pk': obj.pk})
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.has_perm('gallery.change_photo')

    def handle_no_permission(self):
        return redirect('photo_detail', kwargs={'pk': self.get_object().pk})

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'photo_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect('photo_detail', kwargs={'pk': obj.pk})
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.has_perm('gallery.delete_photo')

    def handle_no_permission(self):
        return redirect('photo_detail', kwargs={'pk': self.get_object().pk})

    def get_success_url(self):
        return reverse('home')


class AddFavoriteView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = []

    def form_valid(self, form):
        photo = form.instance
        photo.favorite_users.add(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('home')


class RemoveFavoriteView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = []

    def form_valid(self, form):
        photo = form.instance
        photo.favorite_users.remove(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('home')

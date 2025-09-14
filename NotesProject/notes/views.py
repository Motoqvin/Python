from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from notes.forms import NoteForm
from notes.models import Note


@method_decorator(cache_page(60), name='dispatch')
class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(body__icontains=q))
        tag_slug = self.kwargs.get('slug')
        if tag_slug:
            qs = qs.filter(tags__slug=tag_slug)
        return qs.select_related().prefetch_related('tags')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note-list")

    def form_valid(self, form):
        messages.success(self.request, "Заметка создана")
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Note updated successfully.')
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Note deleted.')
        return super().delete(request, *args, **kwargs)

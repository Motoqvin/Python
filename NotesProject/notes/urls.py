from django.urls import path

from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('notes/create/', views.NoteCreateView.as_view(), name='create'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='edit'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
    path('tags/<slug:slug>/', views.NoteListView.as_view(), name='by_tag'),
    path('search/', views.NoteListView.as_view(), name='search'),
]
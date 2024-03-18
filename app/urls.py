from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),

    # urls for notes
    path('notes/', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delete-note"),
    path('notes_detail/<int:pk>', views.NoteDetailView.as_view(), name="notes-detail"),

    # urls for homework
    path('homework/', views.homework, name="homework"),
    path('update_homework/<int:pk>', views.update_homework, name="update-homework"),
    path('delete_homework/<int:pk>', views.delete_homework, name="delete-homework"),

    # urls for youtube
    path('youtube', views.youtube, name="youtube"),

]

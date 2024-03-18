from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.views.generic import ListView, DetailView

from . models import Notes,Homework

# Create your views here.
#  homePage view 
def home(request):
    return render(request,'app/home.html')

# Notes View 
def notes(request):

    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user = request.user, title = request.POST['title'], description= request.POST['description'])
            notes.save()
        messages.success(request, f"Notes Added {request.user.username} Successfully")

    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    # print(notes)
    context = {'notes' : notes, 'form': form }
    return render(request, 'app/notes.html',context)


# delete note view
def delete_note(reuest, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

# detail view of specified notes
class NoteDetailView(DetailView):
    model = Notes

# Homework view
def homework(request):

    homework_done = False

    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False

            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )

            homeworks.save()
            messages.success(request, f"Homework Added from {request.user.username}!!!!!")

    else:
        form = HomeworkForm()

    homework = Homework.objects.filter(user=request.user)

    if len(homework) == 0:
        homework_done == True
    else:
        homework_done == False

    context = {'homeworks' : homework, "homeworks_done" : homework_done, 'form': form}
    return render(request,'app/homework.html', context)
    
# upadte specific homework 
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)

    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')


# detete specific homework
def delete_homework(reuest, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homework")


# view for seach content on Youtube 
def youtube(request):

    if request.method == 'POST':
        form = AppForm(request.POST)
        text = request.POST['text']
    else:
        form = AppForm()
    context = { 'form': form}
    return render(request, 'app/youtube.html', context)
from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
# from django.core.checks import messages
from django.forms.widgets import FileInput
from django.views.generic import ListView, DetailView
from youtubesearchpython import VideosSearch
from django.contrib.auth.decorators import login_required

from . models import Notes,Homework

# Create your views here.
#  homePage view 
def home(request):
    return render(request,'app/home.html')

# Notes View 
@login_required
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
@login_required
def delete_note(reuest, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")




# detail view of specified notes
class NoteDetailView(DetailView):
    model = Notes




# Homework view
@login_required
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
@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)

    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')




# detete specific homework
@login_required
def delete_homework(reuest, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homework")


# view for seach content on Youtube 
def youtube(request):

    if request.method == 'POST':
        form = AppForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit = 10)
        # print(video.result(), len(video.result()))
        result_list = []

        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            # print(i)
            result_list.append(result_dict)
            # print(len(result_list))
            context = {'form':form, 'results':result_list}

        return render(request, 'app/youtube.html', context)

    else:
        form = AppForm()
    context = { 'form': form}
    return render(request, 'app/youtube.html', context)





# view for todo
@login_required
def todo(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid() == True:
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished =False
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'], 
                 is_finished = finished
            )  
            todos.save()
            messages.success(request, f"Todos Added from {request.user.username}!!!!!")    
    else: 
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)

    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False

    context = { 'todos': todo, 'form':form, 'todos_done': todos_done}
    return render(request, 'app/todo.html', context)





# update todo
@login_required
def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)

    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')





# delete todo
@login_required
def delete_todo(reuest, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect("todo")





# Books view
@login_required
def books(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid() == True:
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished =False
            except:
                finished = False
            books = Books(
                user = request.user,
                title = request.POST['title'], 
                link = request.POST['link'],
                 is_finished = finished
            )  
            books.save()
            messages.success(request, f"e-Books/Articals Added from {request.user.username}!!!!!")    
    else: 
        form = BooksForm()
    book = Books.objects.filter(user=request.user)

    if len(book) == 0:
        done = True
    else:
        done = False

    context = { 'books': book, 'form':form, 'done': done}
    return render(request, 'app/books.html', context)




# update book status
@login_required
def update_book(request, pk=None):
    book = Books.objects.get(id=pk)

    if book.is_finished == True:
        book.is_finished = False
    else:
        book.is_finished = True
    book.save()
    return redirect('books') 




# delete book
@login_required
def delete_book(reuest, pk=None):
    Books.objects.get(id=pk).delete()
    return redirect("books")


# user registration
def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Added Successfully for {username}!!!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'app/register.html',context)




# user profile
@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished = False,user = request.user)
    todos = Todo.objects.filter(is_finished = False,user = request.user)

    if len(homeworks) == 0:
        hw_done = True
    else:
        hw_done =False
    if len(todos) == 0:
        td_done = True
    else:
        td_done =False
    context ={ 'homeworks':homeworks, 'todos':todos, 'hw_done': hw_done, 'td_done': td_done}
    return render(request,'app/profile.html', context)
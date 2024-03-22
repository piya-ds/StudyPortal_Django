from django import forms
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# from to create notes
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title","description"]


# general forms
class DateInput(forms.DateInput):
    input_type = 'date'

class AppForm(forms.Form):
    text = forms.CharField(max_length= 100, label = "Enter Your Search:")

# form to create homework
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ["subject","title","description","due","is_finished"]


#form to create todo list 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","is_finished"]


# form to add eboos/articals
class BooksForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ["title","link","is_finished"]


# UserRegistration form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model: User
        fields: ['username','password1','password2']
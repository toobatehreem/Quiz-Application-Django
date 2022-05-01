from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .models import Quiz, Result

# Create your views here.
def index(request):
    return render(request, 'App/index.html')

def practice(request):
    return render(request, 'App/practice.html')

def pythonquiz(request):
    python_ques = Quiz.objects.raw("SELECT * from App_quiz")
    return render(request, 'App/python.html', context={'python': python_ques})

def csharpquiz(request):
    return HttpResponse("hello to csharp")

def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("App:index")
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid credentials")

    form = AuthenticationForm()
    return render(request=request, template_name='App/login.html', context={'login_form':form})



def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("App:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="App/register.html", context={'register_form':form})


def logoutuser(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect("App:index")


def score(request):
    if request.method == 'POST':
        questions=Quiz.objects.all()
        score=0
        for q in questions:
            if q.answer ==  request.POST.get(q.question):
                score+=10
            elif ''.join(q.answer) == ''.join(request.POST.get(q.question)):
                score+=10
        result = score
        username=request.user
        types = request.POST.get('python').capitalize()
        data = Result(username=username, score=result, types=types)
        data.save()
        return redirect("App:see_results")


def see_results(request):
    user = request.user
    results = Result.objects.filter(username=user)
    return render(request, 'App/results.html', context={'results':results})
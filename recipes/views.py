from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            #create new user
            form.save()

            # login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user =  authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'auth/signup.html', {'form':form})


    else:
        form = UserCreationForm()
        return render(request, "auth/signup.html", {'form':form})
    

def login_view(request):
    #2
    #if request.user.is_authenticated:
    #   return redirect('home')

    #1
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request, user)
            return redirect('home')
    
        else: return render(request, 'auth/login.html', {'form': form})

    else: 
        form = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')




from django.shortcuts import render
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'users/dashboard.html')
        else:
            return render(request, "users/register.html", {'form': form})

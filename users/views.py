from stl_upload.models import UserProcess
from .models import Profile
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
            # create new user
            user = form.save()
            # create new profile
            Profile.objects.create(
                user_id=user.id,
                company=form.cleaned_data['company'],
                address=form.cleaned_data['address'],
                postcode=form.cleaned_data['postcode'],
                country=form.cleaned_data['country']
            )
            # create new userProcss
            UserProcess.objects.create(
                user_id=user.id,
                center_x=0,
                center_y=0,
                center_z=0,
                orientation_x=0.0,
                orientation_y=0.0,
                orientation_z=0.0,
                opacity=1,
                filename='bar_model'
            )
            login(request, user)
            return render(request, 'users/dashboard.html')
        else:
            return render(request, "users/register.html", {'form': form})

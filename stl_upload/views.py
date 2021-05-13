from rest_framework.response import Response

from .serializers import UserProcessSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from .forms import InputsForm
from .models import StlModels, UserProcess, Inputs
import uuid


# Create your views here.
# @login_required
# def upload(request):
#     return render(request, 'upload_step/upload.html')
#

@login_required
def submit_input(request):
    form = {}
    if request.method == 'POST':
        form = InputsForm(request.POST)
        if form.is_valid():
            userProcess = UserProcess.objects.get(user_id=request.user.id)
            stl_models = StlModels.objects.all()

            inputs = Inputs.objects.get(user_id=request.user.id)

            context = {
                'input1': form.cleaned_data['input1'],
                'input2': form.cleaned_data['input2'],
                'input3': form.cleaned_data['input3'],
                'unique_id': str(uuid.uuid4()),
                'stlModels': stl_models,
                'userProcess': userProcess
            }
            print(context)
            return render(request, 'upload_step/upload.html', context)
    elif request.method == "GET":
        form = InputsForm()
    return render(request, 'inputs/input.html', {'form': form})

class UserProcessApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        userProcess = UserProcess.objects.filter(user_id=user_id)
        serializer = UserProcessSerializer(userProcess, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        print(request.data)
        print("------------")
        userProcess = UserProcess.objects.get(user_id=request.data.get('user_id'))
        serializer = UserProcessSerializer(userProcess)
        if serializer.is_valid:
            userProcess.center_x = request.data.get('center_x')
            userProcess.center_y = request.data.get('center_y')
            userProcess.center_z = request.data.get('center_z')
            userProcess.orientation_x = request.data.get('orientation_x')
            userProcess.orientation_y = request.data.get('orientation_z')
            userProcess.orientation_z = request.data.get('orientation_y')
            userProcess.opacity = request.data.get('opacity')
            userProcess.filename = request.data.get('filename')
            userProcess.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

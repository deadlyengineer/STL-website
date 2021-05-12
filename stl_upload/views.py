import re
from .serializers import UserProcessSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.response import JsonResponse
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from .forms import InputsForm
from .models import StlModels, UserProcess
import uuid


# Create your views here.
@login_required
def upload(request):
    return render(request, 'upload_step/upload.html')


@login_required
def submit_input(request):
    form = {}
    if request.method == 'POST':
        form = InputsForm(request.POST)
        if form.is_valid():
            stl_models = StlModels.objects.all()
            context = {
                'input1': form.cleaned_data['input1'],
                'input2': form.cleaned_data['input2'],
                'input3': form.cleaned_data['input3'],
                'unique_id': str(uuid.uuid4()),
                'stlModels': stl_models
            }
            print(context)
            return render(request, 'upload_step/upload.html', context)
    elif request.method == "GET":
        form = InputsForm()
    return render(request, 'inputs/input.html', {'form': form})

class UserProcessApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        userProcess = UserProcess.objects.filter(user = request.user.id)
        serializer = UserProcessSerializer(userProcess[0])
        if serializer.is_valid:
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request, *args, **kwargs):
        print("++++++++");
        print(request)
        data = {
            "user":request.user.id,
            "center_x":request.data.get('center_x'),
            "center_y":request.data.get('center_y'),
            "center_z":request.data.get('center_z'),
            "orientation_x":request.data.get('orientation_x'),
            "orientation_y":request.data.get('orientation_y'),
            "orientation_z":request.data.get('orientation_z'),
            "opacity":request.data.get('opacity'),
            "filename":request.data.get('filename')
        }
        print("+++++++++++")
        print('data')
        serializer = UserProcessSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.data)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

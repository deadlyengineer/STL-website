from rest_framework.response import Response

from .serializers import UserProcessSerializer, UploadStlSerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import InputsForm
from .models import StlModels, UserProcess, Inputs, UserStl
import uuid


# Create your views here.
# @login_required
# def upload(request):
#     return render(request, 'upload_step/upload.html')
#
# @login_required
# def upload_stl(request):
#     form = {}
#     print("SUBMITTED")
#     if request.method == 'POST':
#         form = InputsForm(request.POST)
#         if form.is_valid:
#             myfile = request.FILES['file']
#             print(myfile)
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_url = fs.url(filename)
#             print('Aaaaa===============')
#             print(filename)
#             userStl = UserStl.objects.filter(user_id=request.user.id)
#             if(len(userStl) == 0):
#                 userStl = UserStl.objects.create(
#                     user_id = request.user.id,
#                     stl_file = filename
#                 )
#                 context = {
#                     "userStl": userStl
#                 }
#                 print('create')
#                 return context
#             else:
#                 print('BBBBBB===============')
#                 userStl = userStl.get()
#                 userStl.stl_file = filename
#                 userStl.save()
#                 context = {
#                     "userStl": userStl
#                 }
#                 print('update')
#                 return context


@login_required
def submit_input(request):
    form = {}
    if request.method == 'POST':
        form = InputsForm(request.POST)
        if form.is_valid():
            userProcess = UserProcess.objects.get(user_id=request.user.id)
            stl_models = StlModels.objects.all()
            userStl = UserStl.objects.filter(user_id=request.user.id)
            if(len(userStl) == 0 ):
                userStl = ''
            else:
                userStl = userStl.get()
            print(userStl.file)
            inputs = Inputs.objects.filter(user_id=request.user.id)
            if (len(inputs) == 0):
                inputs = Inputs.objects.create(
                    user_id=request.user.id,
                    input1=form.cleaned_data['input1'],
                    input2=form.cleaned_data['input2'],
                    input3=form.cleaned_data['input3']
                )
            else:
                inputs = inputs.get()
                inputs.input1 = form.cleaned_data['input1']
                inputs.input2 = form.cleaned_data['input2']
                inputs.input3 = form.cleaned_data['input3']
                inputs.save()

            context = {
                'input1': inputs.input1,
                'input2': inputs.input2,
                'input3': inputs.input3,
                'unique_id': str(uuid.uuid4()),
                'stlModels': stl_models,
                'userProcess': userProcess,
                'userStl': userStl
            }
            print("CONTEXT")
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
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadStl(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("WElcome")
        print(request.POST)
        userStl = UserStl.objects.filter(user_id=request.POST.get('user'))
        if(len(userStl) == 0):
            print('none')
            file_serializer = UploadStlSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('Exist')
            userStl = userStl.get()
            userStl.file = request.FILES['file']
            userStl.save()
            file_serializer = UploadStlSerializer(userStl)
            return Response(file_serializer.data, status=status.HTTP_200_OK)

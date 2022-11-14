from django.shortcuts import render, redirect

from .forms import PhonesForm
from .models import Phones
from rest_framework.views import APIView
from .serializers import PhonesSerial
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



def index(request):
    phones = Phones.objects.order_by('surname')
    return render(request, 'main/index.html', {'tittle':'Главная страница', 'phones': phones})

def create(request):
    error = ''
    if request.method == "POST":
        form = PhonesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = PhonesForm()
    return render(request, 'main/create.html', {'form': form, 'error': error})

def delete(request, pk):
    phonebook = Phones.objects.get(id=pk)
    phonebook.delete()
    return redirect('home')


def change(request, pk):
    error =''
    phonebook = Phones.objects.get(id=pk)
    if request.method == "POST":
        form = PhonesForm(request.POST)
        if form.is_valid():
            phonebook.name = form.cleaned_data.get('name')
            phonebook.surname = form.cleaned_data.get('surname')
            phonebook.number = form.cleaned_data.get('number')
            # form.save()
            phonebook.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = PhonesForm()
    return render(request, "main/change.html", {'form': form, 'error': error})


class PhoneViews(APIView):
    def get(self, request, id=None):
        if id is None:
            items = Phones.objects.all()
            serializer = PhonesSerial(items, many=True)
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_200_OK)

    def post(self, request):
        serializer = PhonesSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_200_OK)
        else:
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is None:
            items = Phones.objects.all()
            items.delete()
            return Response({'status': 'success', 'data': 'deleted'}, status.HTTP_200_OK)


class PhonesIdView(APIView):
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(Phones, id=id)
            serializer = PhonesSerial(item)
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            item = get_object_or_404(Phones, id=id)
            item.delete()
            return Response({'status': 'success', 'data': 'deleted'}, status.HTTP_200_OK)

    def patch(self, request, id):
        item = Phones.objects.get(id=id)
        serializer = PhonesSerial(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_200_OK)
        else:
            return Response({'status': 'success', 'data': serializer.data}, status.HTTP_400_BAD_REQUEST)
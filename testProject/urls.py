from ast import excepthandler
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
import requests


def index(request):
    try:
        # if
        # a1 = request.POST['r']
        # print('aaaa', a1)
        # url = "http://192.168.1.86/api/r-ihXRKF7zz2GIg43vj7PrzTQw5EA3NE2seJYWbs/lights/2/state/"
        # a = requests.get(url).json()
        # print('a', a)
        # x = 200
        # # b = '{"bri":'x' }'
        # b = '{"bri":x}'
        # print('b is', b)
        # c = requests.put(url, data=b).json()
        # print('c', c)
        a = request.POST['br']
        print(a)
        return render(request, 'index.html')
    except:
        return render(request, 'index.html')


def brightness(request):
    a = 'nothing'
    print('in brightness')
    return render(request, 'index.html', {'a': a})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('br/', brightness, name="br"),
]

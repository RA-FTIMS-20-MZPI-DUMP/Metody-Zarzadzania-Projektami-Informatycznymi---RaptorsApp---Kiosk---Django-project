import json
import requests
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .forms import KioskTargetPosition, KioskTargetParking
from .models import KioskModel, KioskUser


def get_user(request):
    name = request.user.username
    password = KioskUser.objects.get(name=name).password_api
    return name, password


def get_data_tasks(request):
    name, password = get_user(request)
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/robots/tasks/all'
    result_task = requests.get(url, auth=(name, password))
    return result_task.json()


def data(request):
    return render(request, 'data.html', {'list': get_data_tasks(request)})


def get_data_POI(request):
    name = request.user.username
    password = request.user.password
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/type/parking-types/all'
    result_POI = requests.get(url, auth=(name, password))
    return result_POI.json()


def kiosk_select(request):
    context = {
        'form': KioskModel.objects.all()
    }
    return render(request, 'select.html', context)


def home(request, id):
    kiosk = KioskModel.objects.get(pk=id)
    request.session['wybranykiosk'] = str(kiosk.id)
    return render(request, "home.html", {'wybranykiosk': kiosk})


def poke(request):
    name, password = get_user(request)
    kiosk_id = request.session.get('wybranykiosk', None)
    kiosk = KioskModel.objects.get(pk=kiosk_id)
    j = [{"position": {"x": kiosk.x, "y": kiosk.y, "z": kiosk.z}}]
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/robots/tasks/add'
    requests.post(url, auth=(name, password), json=json.dumps(j, cls=DjangoJSONEncoder))
    context = {
        'form': KioskModel.objects.all()
    }
    return render(request, "home.html", context)


def robot_dismiss(request):
    name, password = get_user(request)
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/robots/tasks/add'
    form = KioskTargetPosition(request.POST or None)
    if form['pozycja'].value() == '1':
        requests.post(url, auth=(name, password), json=[{"position": {
            "x": 2.6013180016895987, "y": -2.0532330810546986, "z": 0}}])
    elif form['pozycja'].value() == '2':
        requests.post(url, auth=(name, password), json=[{"position": {
            "x": -0.8981947615396955, "y": 0.12110796514095412, "z": 0}}])
    elif form['pozycja'].value() == '3':
        requests.post(url, auth=(name, password), json=[{"position": {
            "x": 2.5936465733818803, "y": 2.167727023136999, "z": 0}}])
    if form.is_valid():
        form.save(commit=True)
        form = KioskTargetPosition()
    context = {
        'form': form,
    }
    return render(request, 'robot_dismiss.html', context)


def pomoc(request):
    return render(request, "pomoc.html", {})


def free(request):
    name, password = get_user(request)
    kiosk_id = request.session.get('wybranykiosk', None)
    kiosk = KioskModel.objects.get(pk=kiosk_id)
    j = [{"position": [{"x": kiosk.x, "y": kiosk.y, "z": kiosk.z}]}]
    k = [{"behaviours": [{"name": "SERVICE_GO"}]}]
    url = 'http://adrastea.westus2.cloudapp.azure.com:3333/robots/tasks/add'
    requests.post(url, auth=(name, password), json=json.dumps(j+k, cls=DjangoJSONEncoder))
    context = {
        'form': KioskModel.objects.all()
    }
    return render(request, "home.html", context)

from django.shortcuts import render
from api.classes import Container
from django.http import HttpResponse
import json

# Create your views here.

def api(request):
    if request.method == 'POST':
        try:
            entry = request.POST['entry']
            entry = entry.upper()
            result = [item for item in Container.classes if entry in item]
            return(HttpResponse(formatResult(result)))
        except:
            pass

    return HttpResponse("cool")

def apiget(request, entry):
    entry = entry.upper()
    result = [item for item in Container.classes if entry in item]
    return(HttpResponse(formatResult(result)))

def formatResult(iterable):
    if len(iterable) > 0:
        newIterable = []
        for item in iterable:
            newIterable.append(item)
            x = json.dumps(newIterable)
        return x
    else:
        return "nil"
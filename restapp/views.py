from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from restapp.models import Guitar
import json
from django.views.decorators.csrf import csrf_exempt
def get_guitar_with_id(request, guitar_id):
    if request.method == "GET":
        try:
            guitar = Guitar.objects.get(id=guitar_id)
            guitar_item = {
                "id": guitar.id,
                "name": guitar.name,
                "rank": guitar.rank
            }
            response = json.dumps({'guitar': guitar_item})
        except:
            response = json.dump([{"Error": "There is some problem accrued"}])
    return HttpResponse(response, content_type='text/json')
@csrf_exempt
def guitars_handler(request):
    if request.method == "GET":
        try:
            guitars = Guitar.objects.all()
            results = []
            for item in guitars:
                guitar = {
                    "id": item.id,
                    "name": item.name,
                    "rank": item.rank
                }
                results.append(guitar)
            response = json.dumps({'guitars': results})
        except:
            response = json.dump([{"Error": "There is some problem accrued"}])
        return HttpResponse(response, content_type='text/json')
    
    elif request.method == 'POST':
        payload = json.loads(request.body)
        name = payload.get('name', None)
        rank = payload.get('rank', None)        
        guitar = Guitar(name=name, rank=rank)
        try:
            guitar.save()
            response = json.dumps({'Success': 'Guitar added successfully!'})
        except:
            response = json.dumps({'Error': 'Guitar could not be added!'})
        return HttpResponse(response, content_type='text/json')
    
    else:
        return HttpResponse("Sorry, This method not implemented", content_type='text/json')
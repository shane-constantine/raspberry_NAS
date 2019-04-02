from django.shortcuts import render
from django.http import HttpResponse
import random
import json
from .models import ras_info
import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def data(request):
    data = ras_info.objects.all()[0]
    ajson = []
    ajson.append({"T":str(data.T),
                  "H":str(data.H),
                  "CT":str(data.CT),
                  "CU": str(data.CU),
                  "DT": str(data.DT),
                  "DF": str(data.DF),
                  "DU": str(data.DU),
                  "DP": str(data.DP),
                  "RT": str(data.RT),
                  "RF": str(data.RF),
                  "RU": str(data.RU),
                  "RP": str(data.RP),
                  })
    djson = json.dumps(ajson)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(djson)
    return response

def data_detail(request):
    context = {}
    context['T'] = random.uniform(10, 80)
    context['H'] = random.uniform(10, 100)
    context['CT'] = random.uniform(10, 80)
    context['DT'] = random.uniform(10, 80)
    context['DU'] = random.uniform(10, 80)
    context['DF'] = random.uniform(10, 80)
    context['DP'] = random.uniform(10, 80)
    context['RT'] = random.uniform(10, 80)
    context['RU'] = random.uniform(10, 80)
    context['RF'] = random.uniform(10, 80)
    context['RP'] = random.uniform(10, 80)
    return render(request,"data_page/ras_data.html",context)
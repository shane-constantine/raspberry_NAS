from django.shortcuts import render
from django.http import HttpResponse
import random
import json
from .models import ras_info
import os
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def data(request):
    data = ras_info.objects.all().reverse()[0]
    ajson = []
    ajson.append({"T":data.T,
                  "H":data.H,
                  "CT":data.CT,
                  "CU":data.CU,
                  "DT":data.DT,
                  "DF":data.DF,
                  "DU":data.DU,
                  "DP":data.DP,
                  "RT":data.RT,
                  "RF":data.RF,
                  "RU":data.RU,
                  "RP":data.RP,
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
    context['CU'] = random.uniform(10, 80)
    return render(request,"data_page/ras_data.html",context)

def datas_json(request):
    ajson = []
    number = ras_info.objects.all().count()
    if number >= 200:
        datas = ras_info.objects.all().reverse()[0:200]
        for data in datas:
            ajson.append({"T": data.T,
                          "H": data.H,
                          "CT": data.CT,
                          "CU": data.CU,
                          "DT": data.DT,
                          "DF": data.DF,
                          "DU": data.DU,
                          "DP": data.DP,
                          "RT": data.RT,
                          "RF": data.RF,
                          "RU": data.RU,
                          "RP": data.RP,
                          })
        ajson.reverse()
    else:
        zer = 200 - number
        for i in range(0,zer):
            ajson.append({"T": 0,
                          "H": 0,
                          "CT": 0,
                          "CU": 0,
                          "DT": 0,
                          "DF": 0,
                          "DU": 0,
                          "DP": 0,
                          "RT": 0,
                          "RF": 0,
                          "RU": 0,
                          "RP": 0,
                          })
        datas = ras_info.objects.all()
        for data in datas:
            ajson.append({"T": data.T,
                          "H": data.H,
                          "CT": data.CT,
                          "CU": data.CU,
                          "DT": data.DT,
                          "DF": data.DF,
                          "DU": data.DU,
                          "DP": data.DP,
                          "RT": data.RT,
                          "RF": data.RF,
                          "RU": data.RU,
                          "RP": data.RP,
                          })
    djson = json.dumps(ajson)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(djson)
    return response
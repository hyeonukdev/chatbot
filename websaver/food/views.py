from django.shortcuts import render
from django.core import serializers
import os
import json  # import json module

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def food_menu(request):
    # with open("./food/food_foodmenu.json", "rt", encoding="utf-8") as json_file:
    #     json_data = json.load(json_file)
    # return JsonResponse(json_data, json_dumps_params={"ensure_ascii": False})

    with open("./food/food_foodmenu.json", "rt", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        dump = json.dumps(json_data)
    return HttpResponse(dump, content_type="application/json")


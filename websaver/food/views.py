from django.shortcuts import render

import os
import json  # import json module

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def food_menu(request):
    with open("./food/food_foodmenu.json", "rt", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data, json_dumps_params={"ensure_ascii": False})

import io
import os
from base64 import b64decode
import tensorflow as tf
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from .Classify import *

@csrf_exempt
def classify_api(request):
    data = {"success": False}

    if request.method == "POST":
        tmp_f = NamedTemporaryFile()
        if request.FILES.get("image", None) is not None:
            image_request = request.FILES["image"]
            image_bytes = image_request.read()
            image = Image.open(io.BytesIO(image_bytes))
            image.save(tmp_f, image.format)
        elif request.POST.get("image64", None) is not None:
            base64_data = request.POST.get("image64", None).split(',', 1)[1]
            plain_data = b64decode(base64_data)
            tmp_f.write(plain_data)
        probs = predict(tmp_f)
        tmp_f.close()
        result = list()
        for idx in probs.argsort()[0][::-1][:5]:
            label_string = label_maps_rev[idx].split("-")[-1]
            score =  probs[0][idx]
            result.append([label_string, score])
        if result:
            data["success"] = True
            data["confidence"] = {}
            for res in result:
                data["confidence"][res[0]] = float(res[1])
    return JsonResponse(data)

def classify(request):
    return render(request, 'classify.html', {})

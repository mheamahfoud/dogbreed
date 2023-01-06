import io
import os
from base64 import b64decode
from tensorflow.keras.models import load_model
import tensorflow as tf
from PIL import Image
from django.core.files.temp import NamedTemporaryFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from .Classify import *

model = load_model(os.path.join(settings.MEDIA_ROOT, 'Model/my_model.h5'))
dogchecker = tf.keras.Model(model.input,model.layers[-2].output)

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
        probs,dog_image = predict(tmp_f,model,dogchecker)
        tmp_f.close()
        probs[0][79]=0
        if(dog_image == 0):
            data["message"]="The photo you have submitted doesn't clear, or it does not belong to a dog, kindly resubmit another dog photo"
            return JsonResponse(data)
        max_probs = probs.argsort()[0][::-1][:5]
        res = 100 - sum([int(el * 100) for el in probs[0, max_probs]])
        complement = [res - 4 * (res // 5)] + [res // 5] * 4
        result = list()
        for i in range(len(max_probs)):
            idx = max_probs[i]
            label_string = label_maps_rev[idx].split("-")[-1]
            score =  int(probs[0][idx]*100)+complement[i]
            result.append([label_string, score])
        if result:
            data["success"] = True
            data["confidence"] = {}
            for res in result:
                data["confidence"][res[0]] = (res[1])
    return JsonResponse(data)

def classify(request):
    return render(request, 'classify.html', {})

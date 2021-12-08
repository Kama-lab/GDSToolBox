from django.shortcuts import render
from django.http import HttpResponse
from .pyscripts.ita import convert_to_gds
import json



def home_page(request):
    return render(request,"index.html")

def mobile_page(request):
    return render(request,"mobile.html")

def show_process(request):
    if request.method == "GET":
        input_text = request.GET.get("the_get").split('\n')
        input_type = request.GET.get("input_type")
        gds_format = convert_to_gds(input_text,input_type)
        if gds_format:
            response_data = {
                "output_text": gds_format
            }
        else:
            response_data = {
            "output_text":"Cannot convert"
            }
        print(response_data)
        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"output_text":"nothing to see"}),
            content_type = "application/json"
        )

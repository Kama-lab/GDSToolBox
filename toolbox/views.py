from django.shortcuts import render
from django.http import HttpResponse
from .pyscripts.ita import convert_to_gds
import json



def home_page(request):
    return render(request,"index.html")

def show_process(request):
    if request.method == "GET":
        input_text = request.GET.get("the_get").split('\n')

        response_data = {
            "output_text": convert_to_gds(input_text)
        }
        # output_text = "Hello " + str(input_text)
        # response_data = {
        #     "input_text":input_text,
        #     "output_text": output_text
        # }
        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"output":"nothing to see"}),
            content_type = "application/json"
        )

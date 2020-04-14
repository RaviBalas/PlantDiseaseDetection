from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render
from .predict import  *
import json
import datetime
from rest_framework.decorators import api_view
BASE_DIR='./'

def SaveProfile(request):
    try:
            if request.method == "POST":
                        handle_uploaded_file(request.FILES['imagefile']) 
                        # return_data = {    "error" : "0",     "message" : "sucess",   }
                        return_data = jsonsolution(predict_fun())
            return render(request, 'res.html',{'result':return_data} )
    except Exception as e:
        print("\n++VIEWS.SAVEPROFILE ",str(e),"++\n")
        return {    "error" : str(e),     "message" : "sucess",   }


@api_view(['GET'])
def __index__function(request):
    start_time = datetime.datetime.now()
    elapsed_time = datetime.datetime.now() - start_time
    elapsed_time_ms = (elapsed_time.days * 86400000) + (elapsed_time.seconds * 1000) + (elapsed_time.microseconds / 1000)
    return_data = {
        "error" : "0",
        "message" : "Successful",
        "restime" : elapsed_time_ms
    }
    print("\n\n\n\n__index__function"+str(return_data)+"\n\n\n\n")
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')

@api_view(['POST','GET'])
def predict_plant_disease(request):
    print("++++++++++++++ in predict_plant_disease")
    try:
        if request.method == "GET" :    return_data = {    "error" : "0",    "message" : "Plant Disease Detection [GET REQ] "    }
        else:
            if request.body:
                request_data = request.data["imagefile"]
                print("\n.............................data is Receiveed   base64 \n\n"+str(request_data))
                handle_RestApi_File(request_data)
                return_data = {    "error" : "0",     "message" : "sucess",   }
                return_data.update(jsonsolution(predict_fun()))

            else :  
                    return_data = {    "error" : "1",     "message" : "Request Body is empty",           }
    except Exception as e:
                    print("\n++VIEWS.PREDICT_PLANT_DISEASE ",str(e),"++\n")
                    return_data = {    "error" : "3",     "message" : f"Error : {str(e)}",        }
    print("\n++++++++++++"+str(return_data)+"+++++++++\n")
    return HttpResponse(json.dumps(return_data), content_type='application/json; charset=utf-8')
def index(request) :
    print("+++++++++++++++++++++++=+++++++++Rendring view+++++++++++++++++++++++++++++++")
    return render(request,'upload.html')     
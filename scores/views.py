from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from time import sleep
from .serializers import SituationSerializer

from .algo import pred_func, pred_target

from .models import Situation
# Create your views here.
# from django.http import HttpResponse

# def hello(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)


@csrf_exempt
def app1(request):
    # global res
    res = 0
    innings_no = 1
    over_no =10
    target = 0
    runs = 0
    wickets = 0
    avg_socre = 0
    if request.method == "POST":
        print(request.POST)
        innings_no = int(request.POST.get('innings_no'))
        over_no = int(request.POST.get('over_no'))
        target = int(request.POST.get('target'))
        runs = int(request.POST.get('runs'))
        wickets = int(request.POST.get('wickets'))
        avg_socre = int(request.POST.get('avg_socre'))
        # targets = np.array([[1,target,runs,wickets]])
        if innings_no ==1:
            res = pred_target(over_no,1,runs,wickets)
        elif innings_no ==2:
            res = pred_func(over_no,1,runs,wickets,target)

        if innings_no and over_no and runs and wickets:
            obj = Situation.objects.create(innings_no = innings_no, over_no = over_no, target=target, runs = runs, wickets = wickets, avg_socre = avg_socre)
            obj.save()

    return render(request, 'scores/home.html',{'result': res, 'in':innings_no, 'on':over_no, 'tgt':target, 'rn':runs, 'wk':wickets, 'ag':avg_socre})

'''def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    # red = add('val1','val2')
    res = val1 + val2
    print(res)
    # return render(request,'result.html',{'result': res})
    return render(request,'result.html',{'result': res})'''

class SituationViewSet(viewsets.ModelViewSet):
    queryset = Situation.objects.all().order_by('created_at').reverse()
    # while True:
    #     sleep(1)
    #     update_data()
    # global queryset
    serializer_class = SituationSerializer

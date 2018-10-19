from django.shortcuts import render,reverse, redirect
from django.contrib.auth.decorators import login_required




def gou_wu_che(request):
    if request.method == "GET":
        return render(request, 'shopcar/car_index.html')
    if request.method == "POST":
        # result = request.POST[""]
        pass

def add(request):
    result = request.POST["sh"]


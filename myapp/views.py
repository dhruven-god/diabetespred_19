from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

import pickle

predictor = pickle.load(open('C:/Users/dhruven/Desktop/ML deploy/model.pkl', 'rb'))  

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def predict(request):
    if request.method == 'POST':
        preg = int(request.POST['pregnancies'])
        glucose = int(request.POST['glucose'])
        bp = int(request.POST['bloodpressure'])
        st = int(request.POST['skinthickness'])
        insulin = int(request.POST['insulin'])
        bmi = float(request.POST['bmi'])
        dpf = float(request.POST['dpf'])
        age = int(request.POST['age'])
        
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        prediction = predictor.predict(data)
       
        
        
        return render(request,'myapp/result.html', {'prediction':prediction})
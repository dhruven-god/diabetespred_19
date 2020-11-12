from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import os
#from diabetespred.settings import BASE_DIR
import pickle

CURRENT_DIR = os.path.dirname(__file__)
model_file = os.path.join(CURRENT_DIR, 'model.pkl')
#print(CURRENT_DIR)

predictor = pickle.load(open(model_file, 'rb'))  

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
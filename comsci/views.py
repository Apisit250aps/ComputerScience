from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
import numpy as np
import xlrd


    

# Create your views here.


def homepage(request):
    # name = data['ชื่อ - สกุล']
    # fb = data['Facebook']
    try :
    
        information = pd.read_excel('database/excel/data.xlsx')
        data = pd.DataFrame(information).set_index('ที่')
        pic = {
        'datas': data,
        'ID':data['รหัสนักศึกษา'],
        'prefix':data['คำนำหน้า']

        }
    
    except :
        print("error")
    
    pic = {
        # 'data': data,
        # 'ID':data['รหัสนักศึกษา'],
        # 'prefix':data['คำนำหน้า']
        
        
    }
    
    # print(f'k {name.keys()} : v {name.values()}')
   
    return render(request, 'home.html', pic)

def students(request):
    return render(request, 'students.html')
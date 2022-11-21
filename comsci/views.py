from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import xlrd


# Create your views here.
try:

    information = pd.read_excel('database/excel/data.xlsx')
    data = pd.DataFrame(information).set_index('ที่')
except:
    print("error")


def homepage(request):
    # name = data['ชื่อ - สกุล']
    # fb = data['Facebook']

    pic = {
        'title': 'Home',
        'datas': data,
        'ID': data['รหัสนักศึกษา'],
        'prefix': data['คำนำหน้า'],
        'picture': ['pictures/form-icon.png', 'pictures/lib-logo.png'], 
        'link': ['form', 'lib'], 
        'name': ['Form', 'Library'], 
        'text': ['งาน', 'sskru']

    }
    work = {'picture': ['pictures/form-icon.png', 'pictures/lib-logo.png'],
            'link': ['form', 'lib'], 'name': ['Form', 'Library'], 'text': ['งาน', 'sskru']}

    # print(f'k {name.keys()} : v {name.values()}')

    return render(request, 'home.html', pic)


def form_page(request):
    data = {
        "title": "Form"
    }
    return render(request, 'work_pages/form.html', data)


def students(request):
    main_data = {
        "title": "Student",
        "students":data.head()
        
    }
    print(data)
    return render(request, 'work_pages/students.html', main_data)


def homepage_lib(request):
    data = {
        "title": "Library"
    }
    return render(request, 'work_pages/lib.html', data)


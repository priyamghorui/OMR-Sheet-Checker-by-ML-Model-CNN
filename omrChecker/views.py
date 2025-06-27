from django.shortcuts import render
from django.http import HttpResponse
from .models import MyImage
from .models import outputimage
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from django.conf import settings
import io
import urllib, base64
from django.shortcuts import render
import math
from django.shortcuts import redirect
import json
from omrmodel import classify_bubble_cv2
coordinatesStudentOmr = [
 (120, 767, 201, 1048),
    (251, 764, 333, 1048),
    (383, 764, 465, 1048),
    (516, 764, 597, 1048),
    (648, 764, 729, 1048)
]
coordinatesAnswerKey = [
 (120, 767, 201, 1048),
    (251, 764, 333, 1048),
    (383, 764, 465, 1048),
    (516, 764, 597, 1048),
    (648, 764, 729, 1048)
]
def index(request):
    return render(request,"index.html")


def countbubble(column_regions,thresh):
    num_questions = 50
    num_options = 5
    columns = 5
    questions_per_column = 10
    bubble_matrix = []
    iii=0
    for col_index, (x1, y1, x2, y2) in enumerate(column_regions):
        col_img = thresh[y1:y2, x1:x2]
        h, w = col_img.shape
        # Each column has 30 questions and 4 options per question
        row_height = h // questions_per_column
        option_width = w // num_options

        for i in range(questions_per_column):
            row = []
            for j in range(num_options):
                # Get each bubble
                x_start = j * option_width
                y_start = (i*row_height)+math.floor(i*0.57)
                bubble = col_img[y_start:y_start+row_height, x_start:x_start+option_width]
                # print(bubble)
                white_pixels = cv2.countNonZero(bubble)
                total_pixels = bubble.size
                try:
                    filled_ratio = white_pixels / total_pixels
                except:
                    filled_ratio=0
                filled = 1 if classify_bubble_cv2(bubble) ==1 else 0
                # filled = 1 if filled_ratio > 0.3 else 0
                iii+=1
                row.append(filled)
            bubble_matrix.append(row)
    return bubble_matrix
from PIL import Image
import numpy as np
def getDetails(name):
    path=os.path.join(settings.MEDIA_ROOT, 'uploads', name)
    image = cv2.imread(path)
    image = cv2.resize(image, (800, int(image.shape[0] * 800 / image.shape[1])))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold( blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 11, 2)
    return {'thresh':thresh,'image':image,}
def imageWithOutline(image,column_regions):
    
    for i, (x1, y1, x2, y2) in enumerate(column_regions):
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f'Col {i+1}', (x1 + 5, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    # Assuming image_rgb is a NumPy array (H, W, 3)
    img = Image.fromarray(image.astype('uint8'))  # convert array to image
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return(uri)
def result(matixStudentOmr,matrixAnswerKey):
    correct = 0
    incorrect = 0
    attempt=0
    marks=0 # Every correct +4 and wrong attempt -1
    ans=[]
    for rowStu, rowAns in zip(matixStudentOmr,matrixAnswerKey):
        # print(matixStudentOmr,matrixAnswerKey)
        if rowStu!=[0,0,0,0,0]:
            attempt += 1
            if rowStu == rowAns:
                correct += 1
                marks += 4
                ans.append(1)
            else:
                incorrect += 1
                marks -= 1
                ans.append(0)
        else:
            ans.append(0)

    # print(correct,incorrect, attempt, marks)
    return({'correct':correct,'incorrect':incorrect, 'attempt':attempt, 'marks':marks,'totalQuestion':len(matrixAnswerKey),'ans':ans})


def view_image(request):
    StudentOmrImageName = MyImage.objects.filter(studentName=request.GET.get('studentName')).first().studentOmr.name[8:]
    AnswerKeyImageName = MyImage.objects.filter(studentName=request.GET.get('studentName')).first().answerKey.name[8:]
    detailsStudentOmr=getDetails(StudentOmrImageName)
    detailsAnswerKey=getDetails(AnswerKeyImageName)
    column_regions = [
        (120, 767, 201, 1048),
    (251, 764, 333, 1048),
    (383, 764, 465, 1048),
    (516, 764, 597, 1048),
    (648, 764, 729, 1048)
]
    global coordinatesAnswerKey,coordinatesStudentOmr
    coordinatesStudentOmr=coordinatesAnswerKey=column_regions
    uristudentOmr=imageWithOutline(detailsStudentOmr['image'],column_regions)
    urianswerKey=imageWithOutline(detailsAnswerKey['image'],column_regions)
    matixStudentOmr=countbubble(column_regions,detailsStudentOmr['thresh'])
    matrixAnswerKey=countbubble(column_regions,detailsAnswerKey['thresh'])
    fullResult=result(matixStudentOmr,matrixAnswerKey)
    # print(fullResult['marks'])
    # print(len(fullResult["ans"]))
    combine=zip(fullResult["ans"],matixStudentOmr)
    return render(request, 'view_image.html', {'studentOmr': uristudentOmr,'answerKey':urianswerKey,'matrixAnswerKey': matrixAnswerKey,'matixStudentOmr':matixStudentOmr,'result':fullResult,'ans':combine,'studentName':request.GET.get('studentName')})

def setCordinets(column_regions,columnNo,l,t,r,b):
    arr=[]
    for i, (x1, y1, x2, y2) in enumerate(column_regions):
        if(i==columnNo):
            # print(int(request.POST.get('l')), int(request.POST.get('t')), int(request.POST.get('r')), int(request.POST.get('b')))
            arr.append((l,t,r,b))
            continue
        arr.append((x1, y1, x2, y2))
    return arr
def setPosition(request):
    # print(request.POST.get('column'))
    # print(request.POST.get('identity'))
    global coordinatesStudentOmr,coordinatesAnswerKey
    StudentOmrImageName = MyImage.objects.filter(studentName=request.POST.get('studentName')).first().studentOmr.name[8:]
    AnswerKeyImageName = MyImage.objects.filter(studentName=request.POST.get('studentName')).first().answerKey.name[8:]
    detailsStudentOmr=getDetails(StudentOmrImageName)
    detailsAnswerKey=getDetails(AnswerKeyImageName)
    if(request.POST.get('identity')=='studentOmr'):
        column_regions=coordinatesStudentOmr
        coordinatesStudentOmr=setCordinets(column_regions,int(request.POST.get('column')),int(request.POST.get('l')), int(request.POST.get('t')), int(request.POST.get('r')), int(request.POST.get('b')))
        uristudentOmr=imageWithOutline(detailsStudentOmr['image'],coordinatesStudentOmr)
        urianswerKey=imageWithOutline(detailsAnswerKey['image'],coordinatesAnswerKey)
        matixStudentOmr=countbubble(coordinatesStudentOmr,detailsStudentOmr['thresh'])
        matrixAnswerKey=countbubble(coordinatesAnswerKey,detailsAnswerKey['thresh'])
        fullResult=result(matixStudentOmr,matrixAnswerKey)
        combine=zip(fullResult["ans"],matixStudentOmr)
        return render(request, 'view_image.html', {'studentOmr': uristudentOmr,'answerKey':urianswerKey,'matrixAnswerKey': matrixAnswerKey,'matixStudentOmr':matixStudentOmr,'result':fullResult,'ans':combine,'studentName':request.POST.get('studentName')})
    elif(request.POST.get('identity')=='answerKey'):
        column_regions=coordinatesAnswerKey
        coordinatesAnswerKey=setCordinets(column_regions,int(request.POST.get('column')),int(request.POST.get('l')), int(request.POST.get('t')), int(request.POST.get('r')), int(request.POST.get('b')))
        uristudentOmr=imageWithOutline(detailsStudentOmr['image'],coordinatesStudentOmr)
        urianswerKey=imageWithOutline(detailsAnswerKey['image'],coordinatesAnswerKey)
        matixStudentOmr=countbubble(coordinatesStudentOmr,detailsStudentOmr['thresh'])
        matrixAnswerKey=countbubble(coordinatesAnswerKey,detailsAnswerKey['thresh'])
        fullResult=result(matixStudentOmr,matrixAnswerKey)
        combine=zip(fullResult["ans"],matixStudentOmr)
        return render(request, 'view_image.html', {'studentOmr': uristudentOmr,'answerKey':urianswerKey,'matrixAnswerKey': matrixAnswerKey,'matixStudentOmr':matixStudentOmr,'result':fullResult,'ans':combine,'studentName':request.POST.get('studentName')})

    else:
        return render(request, 'view_image.html', {'studentOmr': 'uristudentOmr','answerKey':'urianswerKey','matrixAnswerKey': 'matrixAnswerKey','matixStudentOmr':'matixStudentOmr','result':'fullResult','ans':'combine','studentName':'N\A'})
        
    
  
from django.http import JsonResponse
def get_columnStudentOmr(request):
    # print(coordinatesStudentOmr)
    col = int(request.GET.get('column', 0))
    # print(f">>>{col}")
    col_data = []
    for i, (x1, y1, x2, y2) in enumerate(coordinatesStudentOmr):
        if(i==col):
            col_data.append(x1)
            col_data.append(y1)
            col_data.append(x2)
            col_data.append(y2)
            break

    return JsonResponse({'t': col_data[1], 'b': col_data[3], 'r': col_data[2], 'l': col_data[0]})
def get_columnAnswerKey(request):

    # print(coordinatesAnswerKey)
    col = int(request.GET.get('column', 0))
    # print(f">>>{col}")
    col_data = []
    for i, (x1, y1, x2, y2) in enumerate(coordinatesAnswerKey):
        if(i==col):
            col_data.append(x1)
            col_data.append(y1)
            col_data.append(x2)
            col_data.append(y2)
            break
    # print(f">>>{col_data}")
    return JsonResponse({'t': col_data[1], 'b': col_data[3], 'r': col_data[2], 'l': col_data[0]})
from django.http import HttpResponseRedirect
def upload_image(request):
    if request.method == 'POST':
        studentName = request.POST.get('studentName')
        studentOmr = request.FILES.get('studentOmr')
        answerKey = request.FILES.get('answerKey')

        # if studentName and studentOmr and answerKey:
        MyImage.objects.create(studentName=studentName, studentOmr=studentOmr,answerKey=answerKey)        
        return HttpResponseRedirect(f'/view?studentName={studentName}')
        # return JsonResponse({'result':'Done'}) 
    return JsonResponse({'result':'error'}) 
# from your_app.models import YourModel
def delDataBase(request):
    MyImage.objects.all().delete()
    return JsonResponse({'result':'Done'}) 



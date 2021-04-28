from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from . import serializers 

def createQP(request):
    if request.method == 'POST':
        form=CreateForm(request.POST)
        if form.is_valid():
            exam=form.cleaned_data.get('exam')
            year=form.cleaned_data.get('year')
            details=form.cleaned_data.get('details')
            numberOfquestion=form.cleaned_data.get('numberOfquestion')
            typeofq=form.cleaned_data.get('typeofq')
            previous_qp=QuestionPaper.objects.filter(exam=exam,year=year,name=details)
            pk=0
            if len(previous_qp)==0:
                qp=QuestionPaper()
                qp.exam=exam
                qp.year=year
                qp.name=details
                qp.total_number_of_questions=0
                qp.total_number_of_questions+=qp.numberOfquestion
                qp.save()
                pk=qp.pk
            else:
                pk=previous_qp[0].pk
            return redirect('upload_q',qp=pk,typeofq=typeofq,numberOfquestion=numberOfquestion)
    elif request.method=='GET':
        form=CreateForm()
    return render(request,'create_q.html',{'form':form})

def uploadQP(request,qp,typeofq,numberOfquestion):

    if request.method == 'POST':
        form=UploadQuestions(extra=numberOfquestion,data=request.POST,files=request.FILES)
        if form.is_valid():
            if typeofq=='SingleCorrect':
                for i in range(numberOfquestion):
                    files=SingleIntegerType()
                    files.QuestionPaper=get_object_or_404(QuestionPaper,pk=qp)
                    files.question=request.FILES['question_%d' % i]
                    files.correct_answer=request.POST['correct_answer_%d' % i]
                    files.QuestionNumber=request.POST['question_number_%d' % i]
                    files.save()
            return redirect('create_q')
    elif request.method=='GET':
        form=UploadQuestions(numberOfquestion)
    return render(request, 'upload_q.html',{'form':form})


@api_view(['GET'])
def question_api(request, question_paper):
    questions=SingleIntegerType.objects.filter(QuestionPaper=question_paper)
    serialize=serializers.QuestionSerializer(questions,many=True)
    return(Response(serialize.data))








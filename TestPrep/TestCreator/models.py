from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import os
from .storage import OverwriteStorage
EXAMS=[
    ('JEE Mains','JEE Mains'),
    ('JEE Advanced','JEE Advanced'),
    ('KVPY','KVPY'),
    ('Bitsat','Bitsat')
]

SINGLE_CORRECT_OPTIONS=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D')
]
SOME_CONST=100

def create_path(instance, filename):
    return os.path.join(str("Questions"),
        instance.QuestionPaper.exam,
        str(instance.QuestionPaper.year),
        instance.QuestionPaper.name,
        str(instance.QuestionNumber)+str(".png")
        
    )

def create_path_user(instance, filename):
    return os.path.join(str("Users"),
        str(instance.user.pk)+str(".png")
        
    )


class QuestionPaper(models.Model):
    exam=models.CharField(max_length=100, choices=EXAMS)
    year=models.IntegerField( null=True, default=2020)
    name=models.CharField(max_length=500,null=True)
    total_number_of_questions=models.IntegerField( null=True, default=0)
    def __str__(self):
        return self.exam+str(self.year)+"_"+self.name

class SingleIntegerType(models.Model):
    question=models.ImageField(upload_to=create_path)
    correct_answer=models.CharField(max_length=10, choices=SINGLE_CORRECT_OPTIONS)
    QuestionNumber = models.IntegerField(null=True)
    QuestionPaper=models.ForeignKey(QuestionPaper, on_delete=models.DO_NOTHING)
    questionType=models.CharField(max_length=100, default="SingleIntegerType", null=True)
    def __str__(self):
        return str(self.QuestionNumber)+"_"+self.QuestionPaper.exam+"_"+str(self.QuestionPaper.year)+"_"+self.QuestionPaper.name
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    userImage=models.ImageField(storage=OverwriteStorage(),upload_to=create_path_user)
    # userAttempts=models.ForeignKey(QuestionPaper, on_delete=models.DO_NOTHING)

class Attempt(models.Model):
    QuestionPaper=models.ForeignKey(QuestionPaper, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class QuestionAttempts(models.Model):
    Attempt=models.ForeignKey(Attempt, on_delete=models.DO_NOTHING,null=True)

    def __init__(self,user_pk,QuestionPaper_pk,question_type, *args, **kwargs):
        super(QuestionAttempts, self).__init__(*args, **kwargs)
        user=get_object_or_404(User,pk=user_pk)
        if question_type=="SingleIntegerType":
            self.answer=models.CharField(max_length=100, choices=SINGLE_CORRECT_OPTIONS,null=True)
        




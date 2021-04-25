from django.db import models
import os

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


def create_path(instance, filename):
    return os.path.join(
        instance.QuestionPaper.exam,
        str(instance.QuestionPaper.year),
        instance.QuestionPaper.name,
        str(instance.QuestionNumber)+str(".png")
        
    )


class QuestionPaper(models.Model):
    exam=models.CharField(max_length=100, choices=EXAMS)
    year=models.IntegerField( null=True, default=2020)
    name=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name

class SingleIntegerType(models.Model):
    question=models.ImageField(upload_to=create_path)
    correct_answer=models.CharField(max_length=10, choices=SINGLE_CORRECT_OPTIONS)
    QuestionNumber = models.IntegerField(null=True)
    QuestionPaper=models.ForeignKey(QuestionPaper, on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.correct_answer)
    
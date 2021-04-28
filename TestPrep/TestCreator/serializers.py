from rest_framework import serializers

from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= SingleIntegerType
        fields=(
            'id','question','correct_answer','QuestionNumber',
            'QuestionPaper',
        )
        read_only_field=(
            'id','question','correct_answer','QuestionNumber',
            'QuestionPaper',
        )
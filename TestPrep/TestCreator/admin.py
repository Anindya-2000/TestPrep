from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(QuestionPaper)
admin.site.register(SingleIntegerType)
admin.site.register(Attempt)
admin.site.register(QuestionAttempts)


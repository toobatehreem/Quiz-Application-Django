from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Lang_Choices = [('python','Python'), ('csharp', 'CSharp')]

class Quiz(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    # name = models.CharField(max_length=50, choices=Lang_Choices, default='python')
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.question

# class Choice(models.Model):
#     question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.choice_text

# class Results(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField()

class Result(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    def __str__(self):
        return self.username.username + " " + self.types + " " + str(self.score)
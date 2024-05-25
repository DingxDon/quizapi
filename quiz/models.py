from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class QuizManager(models.Manager):
    
    def create_Question(self, question, options, correct_option):
        if correct_option not in options:
            raise ValidationError("The Correct option must be selected")
        question_obj = self.create(question=question, options= options, correct_option= correct_option)
        return question_obj
    
class QuizQuestion(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()
    correct_option = models.CharField(max_length=255)
    
    
    objects = QuizManager
    
    def save(self, *args, **kwargs):
        if self.correct_option not in self.options:
            raise ValidationError("The correct option must be selected")
        super().save(*args, **kwargs)
        
        def __str__(self):
            return self.question
        

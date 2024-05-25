from rest_framework import serializers
from .models import QuizQuestion

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = '__all__'
        
    def validate(self, attrs):
        if attrs['correct_option'] not in attrs['options']:
            raise serializers.ValidationError("The correct option must be one of the options.")
        return attrs
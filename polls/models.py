from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200,blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    option1 = models.CharField(max_length=200,default="Option 1",blank=False)
    option2 = models.CharField(max_length=200,default="Option 2",blank=False)
    option3 = models.CharField(max_length=200,default="Option 3",blank=False)
    option4 = models.CharField(max_length=200,default="Option 4",blank=False)
    
    
    def __str__(self):
        return self.question
from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200,blank=False)
    # pub_date = models.DateTimeField('Date Published', null=True)
    no_of_options = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question
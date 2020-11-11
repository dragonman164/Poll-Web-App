from django.shortcuts import render,redirect
from .forms import QuestionForm 
from .models import Question

# Create your views here.
def index(request):
    params = {'Length':len(Question.objects.all())}
    return render(request,'polls/index.html',params)

def create(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/check')
    params = {'form':form}
    return render(request,'polls/create.html',params)

def check(request):
    obj = Question.objects.all()
    params = {'questions':obj}
    return render(request,'polls/check.html',params)

def modify(request,question_id):
    question = Question.objects.get(pk=question_id)
    form = QuestionForm(instance=question)
    if request.method == 'POST':
        form = QuestionForm(request.POST,instance = question)
        if request.POST.get('delete') == '1':
            question.delete()
            return redirect('/check')
        if form.is_valid():
            form.save()
            return redirect('/check')
    

    params = {'form':form}
    return render(request,'polls/modify.html',params)
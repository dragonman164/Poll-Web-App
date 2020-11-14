from django.shortcuts import render,redirect
from .forms import QuestionForm,ParticipantForm
from .models import Question,Participant

# Create your views here.
def index(request):
    params = {'Questions':len(Question.objects.all()),'clients':len(Participant.objects.all())}
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
    form = QuestionForm(instance =question)
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

def participate(request,question_id):
    question = Question.objects.get(pk=question_id)
    participate = Participant(question=question)
    form = ParticipantForm()
    if request.method == 'POST':
        form = ParticipantForm(request.POST,instance = participate)
        if form.is_valid():
            form.save()
            return redirect('/check')
    params = {'Question':question,'form':form}
    return render(request,'polls/participate.html',params)

def results(request,question_id):
    question = Question.objects.get(pk=question_id)
    obj = Participant.objects.all()
    count = {'option1':0,'option2':0,'option3':0,'option4':0}
   
    for elem in obj:
        if question.question == str(elem.question):
            if elem.selected_option == 1:
                count['option1'] += 1
            elif elem.selected_option == 2:
                count['option2'] +=1
            elif elem.selected_option == 3:
                count['option3']+=1
            else:
                count['option4']+=1
    print(count)
    
    params = {'Question':question,'count':count}
    return render(request,"polls/results.html",params)
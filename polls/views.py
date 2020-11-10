from django.shortcuts import render
from .forms import QuestionForm 

# Create your views here.
def index(request):
    return render(request,'polls/index.html')

def create(request):
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    params = {'form':form}
    return render(request,'polls/create.html',params)
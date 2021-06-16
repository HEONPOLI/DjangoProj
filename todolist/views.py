from todolist.forms import TaskForm
from django.shortcuts import render,HttpResponse,redirect
from .forms import TaskForm
from .models import Task
from .mkgantt import mk_gantt, create_gantt
# Create your views here.


def index(request):
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")   #urls.py에 적은 index를 가져온거임

    tasks = Task.objects.all()
    return render(request,"index.html",{"task_form":form,"tasks":tasks})

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method=="POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update_task.html",{"task_edit_form":form})

def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect("index")

def gantt_task(request):
    gantt_tasks = Task.objects.all()
    gantt_tasks_list=list(gantt_tasks)
    task_project = []
    for task in gantt_tasks_list:
        dd=int(Task.objects.get(title=task).start_day)
        dm=int(Task.objects.get(title=task).start_month)
        dy=int(Task.objects.get(title=task).start_year)
        ed=int(Task.objects.get(title=task).end_day)
        em=int(Task.objects.get(title=task).end_month)
        ey=int(Task.objects.get(title=task).end_year)
        task_project.append(mk_gantt(str(task),dd,dm,dy,ed,em,ey))
    create_gantt(task_project)
    # print(gantt_tasks_list)
    # print(1)
    return render(request,"gantt_task.html",{"tasks":gantt_tasks})

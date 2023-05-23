from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        Todo.objects.create(title=title, category=category, description=description)
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_list.html')

def todo_update(request, sno):
    todo = Todo.objects.get(sno=sno)
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        todo.title = title
        todo.category = category
        todo.description = description
        todo.save()
        return redirect("todo:todo_list")
    
    return render(request, 'todo/todo_update.html', {'todo': todo})

def todo_delete(request, sno):
    todo = Todo.objects.get(sno=sno)
    todo.delete()
    return redirect("todo:todo_list")

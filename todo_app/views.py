from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Todo
from .forms import TodoForm, CustomUserCreationForm

# Create your views here.

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Task created successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_app/todo_form.html', {'form': form, 'title': 'Create Task'})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_app/todo_form.html', {'form': form, 'title': 'Update Task'})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('todo_list')
    return render(request, 'todo_app/todo_confirm_delete.html', {'todo': todo})

@login_required
def todo_toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('todo_list')
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

def toggle_theme(request):
    # Get current theme from session or default to light
    current_theme = request.session.get('theme', 'light')
    # Toggle theme
    new_theme = 'dark' if current_theme == 'light' else 'light'
    # Save to session
    request.session['theme'] = new_theme
    # Redirect back to previous page
    return redirect(request.META.get('HTTP_REFERER', 'todo_list'))

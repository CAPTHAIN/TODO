from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import *


def main(request):
    problems = Problem.objects.all()
    return render(request, 'main/index.html', {"problems": problems})


class AddTodo(CreateView):
    form_class = ProblemForm
    template_name = 'main/add.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        new_todo = form.save(commit=False)
        new_todo.author = self.request.user.username
        new_todo.save()
        return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class TodoUpdateView(UpdateView):
    model = Problem
    template_name = 'main/update_page.html'
    slug_url_kwarg = 'post_slug'
    fields = ['title', 'description', 'photo', 'recipient']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoDeleteView(DeleteView):
    model = Problem
    template_name = 'main/delete.html'
    slug_url_kwarg = 'todo_slug'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

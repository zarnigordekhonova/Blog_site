from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsersForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        create_form = UsersForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = UsersForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context=context)

class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {'form': login_form}
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home:home_page_2')
        else:
            context = {'form': login_form}
            return render(request, 'login.html', context=context)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home:home_page')

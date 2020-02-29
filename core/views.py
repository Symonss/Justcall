from django.shortcuts import render, redirect
from core.models import Extension, User
from django.views.generic import CreateView
from core.forms import AdminSignUpForm, UserSignUpForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

def ssignup(request):
    return render(request, 'decide.html',{})

def home(request):

    return render(request, 'home.html', {'extension':extension})
def incoming(request, pk):
    obj = get_object_or_404(Extension, pk=pk)
    print(obj.name)
    return render(request, 'callscreen.html',{'obj':obj})

def admins(request):
    extension = Extension.objects.all()
    return render(request,'admins/home.html',{'extension':extension})

def users_page(request):
    extension = Extension.objects.all()
    
    return render(request,'users/home.html',{'extension':extension})

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins')

class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user_home')
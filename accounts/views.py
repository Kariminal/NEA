from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from .models import *
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

#Views define the model, template and forms to be used for the user.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AreaView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('accounts.add_areas')
    form_class = AddAreaForm
    success_url = reverse_lazy('home')
    template_name = 'AddArea.html'

class AssignVolunteerView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('accounts.add_areas')
    form_class = AreaLinkerForm
    success_url = reverse_lazy('home')
    template_name = 'AssignVolunteer.html'

class CurrentAreas(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = ('accounts.view_areas')
    model = Areas
    template_name = 'Areas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['volunteer'] = Area_Linker.objects.all()
        return context

class DetailsView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'Details.html'
    model = CustomUserChangeForm

    def get_object(self):
        return self.request.user
    #Grabs the current user instance in order to return data specific to them.
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView,TemplateView,UpdateView
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
from .models import Profile
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name="dispatch")
class IndexView(TemplateView):
    template_name = 'accounts/index.html'


class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get(self,request):
        form =  self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('accounts:profile-create')

        return render(request, self.template_name, {'form': form})

class ProfileCreate(CreateView):
    model = Profile
    fields = ['fullname', 'gender', 'branch', 'year', 'session', 'contact_details','accommodation','profile_    photo']
    template_name = 'accounts/create_profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate,self).form_valid(form)
    success_url = reverse_lazy('accounts:index')


class HomeView(ListView):
    model = Profile
    template_name= 'accounts/index.html'

class ProfileView(ListView):
    template_name = 'accounts/profile_form.html'
    context_object_name = 'profile'


    def get_queryset(self):
        return Profile.objects.filter(user = self.request.user)

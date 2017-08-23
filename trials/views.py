from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, ListView, View, TemplateView, DetailView
from .models import ApplyCricket,ApplyBadminton,ApplyFootball,ApplyTugOfWar,ApplyAthletics,ApplyBasketBall,ApplyVolleyBall,ApplyChess,ApplyCarrom,ApplyTableTennis
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from .forms import ApplyCricketForm,ApplyBadmintonForm,ApplyTugOfWarForm,ApplyAthleticsForm,ApplyFootballForm,ApplyBasketballForm,ApplyVolleyballForm,ApplyChessForm,ApplyCarromForm,ApplyTableTennisForm
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required


# class ApplyView(CreateView):
#     model = Apply
#     fields = ['name', 'cricket', 'badminton', 'football', 'basketball', 'volleyball','chess','carrom','table_tennis','tug_of_war','athletics']
#     template_name = 'trials/apply_form.html'
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ApplyView, self).form_valid(form)
#     success_url = reverse_lazy('accounts:index')
#
#
class ViewApplications(TemplateView):
    template_name = 'trials/sports_list.html'

# class ApplicationsList(ListView):
#     template_name = 'trials/applications.html'
#     context_object_name = 'applications'
#
#     def get_queryset(self):
#         return Apply.objects.all()

class ViewApplicationsCricket(ListView):
    template_name = 'trials/applications_game_wise_cricket.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyCricket.objects.all()


class ViewApplicationsBadminton(ListView):
    template_name = 'trials/applications_game_wise_badminton.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyBadminton.objects.all()

class ViewApplicationsFootball(ListView):
    template_name = 'trials/applications_game_wise_football.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyFootball.objects.all()
#
class ViewApplicationsBasketball(ListView):
    template_name = 'trials/applications_game_wise_basketball.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyBasketBall.objects.all()

class ViewApplicationsVolleyball(ListView):
    template_name = 'trials/applications_game_wise_volleyball.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyVolleyBall.objects.all()
#
class ViewApplicationsChess(ListView):
    template_name = 'trials/applications_game_wise_chess.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyChess.objects.filter(chess=True)
#
class ViewApplicationsCarrom(ListView):
    template_name = 'trials/applications_game_wise_carrom.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyCarrom.objects.all()
#
class ViewApplicationsTableTennis(ListView):
    template_name = 'trials/applications_game_wise_table_tennis.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyTableTennis.objects.all()
#
class ViewApplicationsTugOfWar(ListView):
    template_name = 'trials/applications_game_wise_tug_of_war.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyTugOfWar.objects.all()
#
class ViewApplicationsAthletics(ListView):
    template_name = 'trials/applications_game_wise_athletics.html'
    context_object_name = 'app_game'

    def get_queryset(self):
        return ApplyAthletics.objects.all()

def SelectedCricket(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyCricket.objects.get(pk=int(key.replace('app',''))-1)
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_cricket.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedBadminton(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyBadminton.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_badminton.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedFootball(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyFootball.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_football.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedBasketball(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyBasketBall.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_basketball.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedVolleyball(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyVolleyBall.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_volleyball.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedChess(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyChess.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_chess.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedCarrom(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                selected_user=ApplyCarrom.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_carrom.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedTableTennis(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                selected_user=ApplyTableTennis.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_table_tennis.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedTugOfWar(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyTugOfWar.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_tug_of_war.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

def SelectedAthletics(request):
    try:
        for key in request.POST.keys():
            if 'app' in key:
                print(int(key.replace('app',''))+1)
                selected_user=ApplyAthletics.objects.get(pk=int(key.replace('app','')))
                selected_user.status = True
                selected_user.save()
        return HttpResponse("Players Selected")

        # selected_user = ApplyCricket.objects.get(pk=request.POST('app'))
    except (KeyError, User.DoesNotExist):
        return render(request,'trials/applications_game_wise_athletics.html',{
            'error_message':"kjebfiwhuefnwne"
        })
    return HttpResponse("Players Selected")

@method_decorator(login_required,name="dispatch")
class ApplyView(TemplateView):
    template_name = 'trials/sports_list.html'

@method_decorator(login_required, name="dispatch")
class ApplyCricketView(View):
    form_class = ApplyCricketForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cricket = form.save(commit=False)
            cricket.user = request.user
            cricket.fullname =Profile.objects.get(user=request.user).fullname
            cricket.cricket = True
            cricket.player_type = form.cleaned_data['player_type']
            cricket.preferred_hand = form.cleaned_data['preferred_hand']
            cricket.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyBadmintonView(View):
    form_class = ApplyBadmintonForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            badminton = form.save(commit=False)
            badminton.user = request.user
            badminton.fullname = Profile.objects.get(user=request.user).fullname
            badminton.badminton = True
            badminton.preferred_hand = form.cleaned_data['preferred_hand']
            badminton.past = form.cleaned_data['past']
            badminton.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyFootballView(View):
    form_class = ApplyFootballForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            football = form.save(commit=False)
            football.user = request.user
            football.fullname = Profile.objects.get(user=request.user).fullname
            football.football = True
            football.left_of_right = form.cleaned_data['left_or_right']
            football.position = form.cleaned_data['position']
            football.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyBasketballView(View):
    form_class = ApplyBasketballForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            basketball = form.save(commit=False)
            basketball.user = request.user
            basketball.fullname = Profile.objects.get(user=request.user).fullname
            basketball.basketball = True
            basketball.past = form.cleaned_data['past']
            basketball.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyVolleyballView(View):
    form_class = ApplyVolleyballForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            volleyball = form.save(commit=False)
            volleyball.user = request.user
            volleyball.fullname = Profile.objects.get(user=request.user).fullname
            volleyball.volleyball = True
            volleyball.past = form.cleaned_data['past']
            volleyball.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyChessView(View):
    form_class = ApplyChessForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            chess = form.save(commit=False)
            chess.user = request.user
            chess.fullname = Profile.objects.get(user=request.user).fullname
            chess.chess = True
            chess.past = form.cleaned_data['past']
            chess.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyCarromView(View):
    form_class = ApplyCarromForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            carrom = form.save(commit=False)
            carrom.user = request.user
            carrom.fullname = Profile.objects.get(user=request.user).fullname
            carrom.carrom = True
            carrom.past = form.cleaned_data['past']
            carrom.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})


@method_decorator(login_required, name="dispatch")
class ApplyTableTennisView(View):
    form_class = ApplyTableTennisForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            table_tennis = form.save(commit=False)
            table_tennis.user = request.user
            table_tennis.fullname = Profile.objects.get(user=request.user).fullname
            table_tennis.table_tennis = True
            table_tennis.past = form.cleaned_data['past']
            table_tennis.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyTugOfWarView(View):
    form_class = ApplyTugOfWarForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            tug_of_war = form.save(commit=False)
            tug_of_war.user = request.user
            tug_of_war.fullname = Profile.objects.get(user=request.user).fullname
            tug_of_war.tug_of_war = True
            tug_of_war.past = form.cleaned_data['past']
            tug_of_war.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name="dispatch")
class ApplyAthleticsView(View):
    form_class = ApplyAthleticsForm
    template_name = 'trials/cricket.html'

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            athletics = form.save(commit=False)
            athletics.user = request.user
            athletics.fullname = Profile.objects.get(user=request.user).fullname
            athletics.athletics = True
            athletics.past = form.cleaned_data['past']
            athletics.save()
            return redirect('accounts:index')
        return render(request,self.template_name,{'form':form})

from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,View
from .models import Sports,Teams,ScheduleCricket,PointsTableCricket
from .forms import ScheduleCricketForm
from django.http import HttpResponse
import itertools
import datetime
import random
# Create your views here.

class IndexView(TemplateView):
    template_name = 'saksham17/index.html'

class SportsAddView(CreateView):
    model = Sports
    fields = ['name','type']
    template_name = 'saksham17/create_sports.html'

class TeamsListView(ListView):
    context_object_name = 'teams'
    template_name = 'saksham17/teams_list.html'

    def get_queryset(self):
        return Teams.objects.all()

class TeamsDetailView(DetailView):
    model = Teams
    template_name = 'saksham17/teams_details.html'

class TeamsAddView(CreateView):
    model = Teams
    fields = ['branch_initials','branch_name']
    template_name = 'saksham17/create_teams.html'

class SportsView(ListView):
    context_object_name = 'sports'
    template_name = 'saksham17/sports_list.html'

    def get_queryset(self):
        return Sports.objects.all()

class SportsDetailView(DetailView):
    model = Sports
    template_name = 'saksham17/sports_details.html'

class ScheduleCricketView(View):
    template_name = 'saksham17/schedule_cricket.html'
    form_class = ScheduleCricketForm
    list1 = []

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    for primary in range(1,len(Teams.objects.all())+1):
        initials = Teams.objects.get(pk=primary).branch_initials
        list1.append(initials)

    if('EI' and 'CE') in list1:
        for n,i in enumerate(list1):
            if i == 'EI':
                list1[n] = 'CE + EI'

            elif i == 'MBA':
                list1[n] = 'MBA + MCA'

        del(list1[list1.index('CE')])
        del(list1[list1.index('MCA')])

        def post(self,request):
            j = 0
            matches = list(itertools.combinations(self.list1,2))
            random.shuffle(matches)
            for i in matches:
                j = j+1
                form = self.form_class(request.POST)
                sch = form.save(commit=False)
                sch.date = sch.starting_date + datetime.timedelta(days=j)
                sch.host = i[0]
                sch.opponent = i[1]
                sch.starting_date = form.cleaned_data['starting_date']
                sch.match_no =  sch.match_no + j
                sch.save()
            return render(request,self.template_name,{'form':form})

class ViewScheduleCricketList(ListView):
    template_name = 'saksham17/view_schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        return ScheduleCricket.objects.all().order_by('match_no')

class ViewScheduleCricketDetail(DetailView):
    model = ScheduleCricket
    template_name = 'saksham17/match_details.html'

def SetWinnerCricket(request):
    match_id = request.POST.get("match","")
    selected_match = ScheduleCricket.objects.get(pk=match_id)
    list1 = [selected_match.host,selected_match.opponent]

    selected_match.winner = request.POST.get("winner_value")

    if selected_match.winner == "tie":
        selected_match.winner = "Match Tied"
        selected_match.runner_up = "Match Tied"

        points_winner = PointsTableCricket.objects.get(team=selected_match.host)
        points_runner_up = PointsTableCricket.objects.get(team=selected_match.opponent)

        points_winner.matches_played = points_winner.matches_played + 1
        points_runner_up.matches_played = points_runner_up.matches_played + 1

        points_winner.tie = points_runner_up.tie + 1
        points_runner_up.tie = points_runner_up.tie + 1

        points_winner.points = points_winner.points + 1
        points_runner_up.points = points_runner_up.points + 1

        points_winner.save()
        points_runner_up.save()
        selected_match.save()

    elif selected_match.winner == "no":
        selected_match.winner = "No Result"
        selected_match.runner_up = "No Result"

        points_winner = PointsTableCricket.objects.get(team=selected_match.host)
        points_runner_up = PointsTableCricket.objects.get(team=selected_match.opponent)

        points_winner.matches_played = points_winner.matches_played + 1
        points_runner_up.matches_played = points_runner_up.matches_played + 1

        points_winner.tie = points_runner_up.tie + 1
        points_runner_up.tie = points_runner_up.tie + 1

        points_winner.points = points_winner.points + 1
        points_runner_up.points = points_runner_up.points + 1

        points_winner.save()
        points_runner_up.save()
        selected_match.save()

    else:
        points_winner = PointsTableCricket.objects.get(team=selected_match.winner)
        points_winner.matches_played = points_winner.matches_played + 1
        points_winner.won = points_winner.won + 1
        points_winner.points = points_winner.points + 2

        del (list1[list1.index(selected_match.winner)])
        selected_match.runner_up = list1[0]

        points_runner_up = PointsTableCricket.objects.get(team=selected_match.runner_up)
        points_runner_up.matches_played = points_runner_up.matches_played + 1
        points_runner_up.lost = points_runner_up.lost + 1
        points_winner.save()
        points_runner_up.save()
        selected_match.save()

    selected_match.played = True
    return HttpResponse("Winner is " + selected_match.winner)


class CreateCricketTable(CreateView):
    template_name = 'saksham17/cricket_table.html'
    model = PointsTableCricket
    fields = ['team']

class PointsTableCricketView(ListView):
    template_name = 'saksham17/points_table_cricket.html'
    context_object_name = 'table'

    def get_queryset(self):
        return PointsTableCricket.objects.all().order_by('-points')

def CricketKnockoutSchedule(request):

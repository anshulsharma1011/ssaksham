from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,View
from .models import Sports,Teams,ScheduleCricket
from .forms import ScheduleCricketForm
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
                list1[n] = 'EI+CE'
                break;
            elif i == 'MBA':
                list1[n] = 'MBA+MCA'
                break;
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

import itertools
from django.shortcuts import render
from django.views.generic import ListView,CreateView,View
from django.shortcuts import redirect
# Create your views here.
from .forms import ScheduleCricketForm
from .models import ScheduleCricket
from django.db import transaction
import datetime


class IndexView(View):
    template_name = 'schedule/schedule_cricket.html'
    form_class = ScheduleCricketForm

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        j = 0
        h = ['CSE','IT','ECE','ME','CE+EI','EN','MBA+MCA']
        matches = list(itertools.combinations(h,2))
        for i in matches:
            j = j+1
            form = self.form_class(request.POST)
            sch = form.save(commit=False)
            sch.closing_date = form.cleaned_data['closing_date']
            sch.starting_date = sch.starting_date + datetime.timedelta(days=j)
            sch.host = i[0]
            sch.opponent = i[1]
            sch.save()

        return render(request,self.template_name,{'form':form})


class ViewSchedule(ListView):
    template_name = 'schedule/view_schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        return ScheduleCricket.objects.all()


from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'trials'

urlpatterns = [

    url(r'^apply/$', views.ViewApplications.as_view(), name='apply'),

    url(r'^applications/$', views.ViewApplications.as_view(), name='applications_list'),

    url(r'^applications/cricket/$', views.ViewApplicationsCricket.as_view(), name='applications_cricket'),
    url(r'^applications/badminton/$', views.ViewApplicationsBadminton.as_view(), name='applications_badminton'),
    url(r'^applications/football/$', views.ViewApplicationsFootball.as_view(), name='applications_football'),
    url(r'^applications/basketball/$', views.ViewApplicationsBasketball.as_view(), name='applications_basketball'),
    url(r'^applications/volleyball/$', views.ViewApplicationsVolleyball.as_view(), name='applications_volleyball'),
    url(r'^applications/chess/$', views.ViewApplicationsChess.as_view(), name='applications_chess'),
    url(r'^applications/carrom/$', views.ViewApplicationsCarrom.as_view(), name='applications_carrom'),
    url(r'^applications/table_tennis/$', views.ViewApplicationsTableTennis.as_view(), name='applications_table_tennis'),
    url(r'^applications/tug_of_war/$', views.ViewApplicationsTugOfWar.as_view(), name='applications_tug_of_war'),
    url(r'^applications/athletics/$', views.ViewApplicationsAthletics.as_view(), name='applications_athletics'),


    url(r'^apply/cricket/$', views.ApplyCricketView.as_view(), name='apply_cricket'),
    url(r'^apply/badminton/$', views.ApplyBadmintonView.as_view(), name='apply_badminton'),
    url(r'^apply/football/$', views.ApplyFootballView.as_view(), name='apply_football'),
    url(r'^apply/basketball/$', views.ApplyBasketballView.as_view(), name='apply_basketball'),
    url(r'^apply/volleyball/$', views.ApplyVolleyballView.as_view(), name='apply_volleyball'),
    url(r'^apply/chess/$', views.ApplyChessView.as_view(), name='apply_chess'),
    url(r'^apply/carrom/$', views.ApplyCarromView.as_view(), name='apply_carrom'),
    url(r'^apply/table_tennis/$', views.ApplyCarromView.as_view(), name='apply_table_tennis'),
    url(r'^apply/tug_of_war/$', views.ApplyCarromView.as_view(), name='apply_tug_of_war'),
    url(r'^apply/athletics/$', views.ApplyCarromView.as_view(), name='apply_athletics'),


    url(r'^apply/cricket/selected/cricket/$',views.SelectedCricket,name='selected'),
    url(r'^apply/cricket/selected/badminton/$',views.SelectedBadminton,name='selected_badminton'),
    url(r'^apply/cricket/selected/football/$',views.SelectedFootball,name='selected_football'),
    url(r'^apply/cricket/selected/basketball/$',views.SelectedBasketball,name='selected_basketball'),
    url(r'^apply/cricket/selected/volleyball/$',views.SelectedVolleyball,name='selected_volleyball'),
    url(r'^apply/cricket/selected/chess/$',views.SelectedChess,name='selected_chess'),
    url(r'^apply/cricket/selected/carrom/$',views.SelectedCarrom,name='selected_carrom'),
    url(r'^apply/cricket/selected/table_tennis/$',views.SelectedTableTennis,name='selected_table_tennis'),
    url(r'^apply/cricket/selected/tug_of_war/$',views.SelectedTugOfWar,name='selected_tug_war'),
    url(r'^apply/cricket/selected/athletics/$',views.SelectedAthletics,name='selected_athletics'),

]

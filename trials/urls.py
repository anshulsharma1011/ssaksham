from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'trials'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^apply/$', views.ApplyView.as_view(), name='apply'),
    # url(r'^applications/all/$', views.ApplicationsList.as_view(), name='view_applications'),
    url(r'^applications/$', views.ViewApplications.as_view(), name='applications_list'),
    url(r'^applications/cricket/$', views.ViewApplicationsCricket.as_view(), name='applications_cricket'),
    url(r'^applications/badminton/$', views.ViewApplicationsBadminton.as_view(), name='applications_badminton'),
    url(r'^applications/football/$', views.ViewApplicationsFootball.as_view(), name='applications_football'),
    # url(r'^applications/basketball/$', views.ViewApplicationsBasketball.as_view(), name='applications_basketball'),
    # url(r'^applications/volleyball/$', views.ViewApplicationsVolleyball.as_view(), name='applications_volleyball'),
    # url(r'^applications/chess/$', views.ViewApplicationsChess.as_view(), name='applications_chess'),
    # url(r'^applications/carrom/$', views.ViewApplicationsCarrom.as_view(), name='applications_carrom'),
    # url(r'^applications/table_tennis/$', views.ViewApplicationsTableTennis.as_view(), name='applications_table_tennis'),
    # url(r'^applications/tug_of_war/$', views.ViewApplicationsTugOfWar.as_view(), name='applications_tug_of_war'),
    # url(r'^applications/athletics/$', views.ViewApplicationsAthletics.as_view(), name='applications_athletics'),
    url(r'^apply/cricket/$', views.ApplyCricketView.as_view(), name='apply_cricket'),
    url(r'^apply/badminton/$', views.ApplyBadmintonView.as_view(), name='apply_badminton'),
    url(r'^apply/football/$', views.ApplyFootballView.as_view(), name='apply_football'),
    url(r'^apply/basketball/$', views.ApplyBasketballView.as_view(), name='apply_basketball'),
    url(r'^apply/volleyball/$', views.ApplyVolleyballView.as_view(), name='apply_volleyball'),
    url(r'^apply/chess/$', views.ApplyChessView.as_view(), name='apply_chess'),
    url(r'^apply/carrom/$', views.ApplyCarromView.as_view(), name='apply_carrom'),
    url(r'^apply/tabletennis/$', views.ApplyCarromView.as_view(), name='apply_tabletennis'),
]

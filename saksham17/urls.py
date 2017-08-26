from django.conf.urls import url
from . import views

app_name = 'saksham17'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^sports/$',views.SportsView.as_view(),name='sports_list_view'),
    url(r'^sports/add/$',views.SportsAddView.as_view(),name='sports_add'),
    url(r'^sports/(?P<pk>[0-9]+)/$',views.SportsDetailView.as_view(),name='sports_details'),

    url(r'^teams/add/$',views.TeamsAddView.as_view(),name='teams_add'),
    url(r'^teams/$',views.TeamsListView.as_view(),name='teams_list'),
    url(r'^teams/(?P<pk>[0-9]+)/$',views.TeamsDetailView.as_view(),name='teams_details'),

    url(r'^schedule/create/cricket/$',views.ScheduleCricketView.as_view(),name='schedule_cricket'),
    url(r'^schedule/view/cricket/$',views.ViewScheduleCricketList.as_view(),name='schedule_view'),
    url(r'^schedule/view/cricket/(?P<pk>[0-9]+)/$',views.ViewScheduleCricketDetail.as_view(),name='schedule_details'),
    url(r'^schedule/view/cricket/winner/',views.SetWinnerCricket,name='set_winner_cricket'),

    url(r'^points_table/create/cricket/',views.CreateCricketTable.as_view(),name='points_table_create_cricket'),
    url(r'^points_table/view/cricket/',views.PointsTableCricketView.as_view(),name='points_table_cricket')

]

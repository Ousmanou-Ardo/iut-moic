from django.urls import path
from . import views

app_name = 'oic'
urlpatterns = [
path('', views.index, name='index'),
#path('learders/', views.executives,name='lea'),
#path('', views.ExecutiveDetailView.as_view(), name='executive_details'),
#path('executive/', view=views.ExecutiveListView.as_view(), name='executive'),
]
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('Add_Area/', views.AreaView.as_view(), name='add_area'),
    path('Areas/',views.CurrentAreas.as_view(), name='existing_areas'),
    path('Details/',views.DetailsView.as_view(), name='details'),
    path('AssignVolunteer/',views.AssignVolunteerView.as_view(), name='add_vol'),
]
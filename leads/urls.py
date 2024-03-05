
from django.urls import path
from .views import leads_list, lead_detail, lead_create

app_name ="leads"

urlpatterns = [
    path('', leads_list),
    path('<int:pk>/', lead_detail),
    path('create/', lead_create),
]
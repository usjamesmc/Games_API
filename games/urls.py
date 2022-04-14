from django.urls import path
from . import views

urlpatterns = [     
    path('', views.games_list),
    path('<int:pk>/', views.game_detail)
]
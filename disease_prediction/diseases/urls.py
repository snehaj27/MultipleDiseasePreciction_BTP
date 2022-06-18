from django.urls import path
from . import views

urlpatterns = [
    path('heart-disease/', views.heart, name="heart_disease"),
    path('liver-disease/', views.liver, name="liver_disease"),
    path('kidney-disease/', views.kidney, name="kidney_disease"),
    path('diabetes/', views.diabetes, name="diabetes"),
    path('breast-cancer/', views.breastCancer, name="breast_cancer")

]

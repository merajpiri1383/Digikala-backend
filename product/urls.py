from django.urls import path
from product import views

urlpatterns = [
    path("color/",views.CreateColorAPIView.as_view(),name="list-create-color"),
    path("color/<int:pk>/",views.ColorAPIView.as_view(),name="detail-color")
]
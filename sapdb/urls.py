from django .urls import path
from sapdb import views


urlpatterns = [
   path("sapdbproduct/",views.Productdbview.as_view()),
   path('sapdbproduct/<int:id>/',views.Productdbindividualview.as_view())                 
]
from django.urls import path
from accounts import views


urlpatterns = [
  path('register/',views.RegisterView.as_view()),
  path('update/<int:pk>', views.updateRegister.as_view()),
  path('delete/<int:pk>', views.deleteRegister.as_view()),
  path('userAuthVerify', views.userAuthVerify.as_view()),
  # path('logInController',views.logInController.as_view())
  
  path('history/',views.HistoryView.as_view()),
  path('history/delete/<int:pk>',views.deleteHistory.as_view())
]
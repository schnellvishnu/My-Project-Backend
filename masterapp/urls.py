from django.urls import path
from  . import views


urlpatterns = [
  path('company/', views.CompanyView.as_view()),
    path('company/update/<int:pk>', views.updateCompany.as_view()),
    path('company/delete/<int:pk>', views.deleteCompany.as_view()),
    path('company/<int:id>/',views.Companyindividual.as_view()),
# __________________________________________________________________
    path('customer/', views.CustomersView.as_view()),
    path('customer/update/<int:pk>', views.updateCustomer.as_view()),
    path('customer/delete/<int:pk>', views.deleteCustomer.as_view()),
    path('customer/<int:id>/',views. CustomerViewIndividual.as_view()),
    
    path('products/', views.ProductView.as_view()),
    path('products/<int:id>/',views.Productindividual.as_view()),
    path('products/update/<int:pk>', views.updateProduct.as_view()),
    path('products/delete/<int:pk>', views.deleteProduct.as_view()),
    #----------------------------------------------------------------------------
    path('shippo/', views.ShipPOView.as_view()),
    path('shippo/update/<int:pk>', views.updateShipPO.as_view()),
    path('shippo/delete/<int:pk>', views.deleteShipPO.as_view()),
    path('shippo/<int:id>/',views.ShippoViewIndividual.as_view()),
    
    path('stock/', views.StockView.as_view()),
    path('stock/update/<int:pk>', views.updateStock.as_view()),
    path('stock/delete/<int:pk>', views.deleteStock.as_view()),
    path('stock/closed', views.Stockclosedview.as_view()),
]
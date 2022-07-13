from django.urls import path
from app import views

urlpatterns = [
  path('', views.IndexView.as_view(), name="index"),
  path('detail/<slug>', views.ItemDetailView.as_view(), name='detail'),
  path('additem/<slug>', views.addItem, name='additem'),
  path('order/', views.OrderView.as_view(), name='order'),
  path('removeitem/<slug>', views.removeItem, name='removeitem'),
  path('removesingleitem/<slug>', views.removeSingleItem, name='removesingleitem'),
  path('payment/', views.PaymentView.as_view(), name='payment'),
  path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
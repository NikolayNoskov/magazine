'''
урлы приложения
'''
from django.urls import path
#from .views import index, by_dep
#from .views import ContactCreateView, DepartamentCreateView
from . import views
urlpatterns = [
    #path('adddep/', DepartamentCreateView.as_view(), name='adddep'),    
    #path('add/', ContactCreateView.as_view(), name='add'),
    #path('by_dep<int:dep_id>/', by_dep, name='by_dep'),
    path(r'landing/', views.landing, name='landing'),
]

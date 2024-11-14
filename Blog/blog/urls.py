from django.urls import path  # Correct import for URL routing
from . import views

urlpatterns = [
    path('', views.home_page,name='home'),
    path('view/<int:pk>', views.View,name='view'),
    path('edit/<int:pk>', views.Edit,name='edit'),
    path('delete/<int:pk>', views.Delete,name='delete'),
    path('add', views.add,name='add'),
    
    #category
    path('tech/<slug:val>', views.tech,name='tech'),
    path('health/<slug:val>', views.health,name='health'),
    path('travel/<slug:val>', views.travel,name='travel'),
    path('food/<slug:val>', views.food,name='food'),
    path('lifestyle/<slug:val>', views.lifestyle,name='lifestyle'),

    path('search', views.search,name='search'),

]
from django.urls import path
from B_app import views

#template tagging
app_name = 'B_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]




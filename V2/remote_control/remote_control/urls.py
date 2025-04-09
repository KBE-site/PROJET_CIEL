from django.urls import path, include

urlpatterns = [
    path('informations/', include('informations.urls'), name='informations')
]

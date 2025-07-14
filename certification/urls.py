from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *
from .views import CareerOpportunitiesView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("certif/", certification_list, name="certification_list"),
    path('certif_detail/<int:pk>/', certification_detail, name='certification_detail'),

    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
    #path("certification/<int:pk>/", CertificationDetailView.as_view(), name="certification_detail"),
    path("careers/", CareerOpportunitiesView.as_view(), name="career_opportunities"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

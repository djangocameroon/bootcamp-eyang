from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import IndexView, AddCertificationView, AddRelatedView, CertificationDetailView, login, registration, logout

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
    path("certification/<int:pk>/", CertificationDetailView.as_view(), name="certification_detail"),
    path('login/',views.login, name= 'login'),
    path('registration/',views.registration, name= 'registration'),
    path('logout',views.logout, name= 'logout'),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(), 
         name='password_reset'),#password reset urls
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),#password reset urls
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),#password reset urls
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'), #password reset urls
    # path('accounts/', include('allauth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

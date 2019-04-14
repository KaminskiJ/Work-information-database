"""work_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from knowledgebank.views import Home, CountryEntryCreateView, ClientEntryCreateView, CountryDetails, ClientList, QuestionsList, CreateQuestion, ClientDetails, CountriesList, AddNewClient, AddNewCountry
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('addcountry/', AddNewCountry.as_view(), name='new-country'),
    path('addclient/', AddNewClient.as_view(), name='new-client'),
    path('country/new', CountryEntryCreateView.as_view(), name='new-country-info'),
    path('client/new', ClientEntryCreateView.as_view(), name='new-client-info'),
    path('countries/', CountriesList.as_view(), name='countries'),
    path('countries/<int:country_id>/', CountryDetails.as_view(), name='client-detail'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('clients/<int:client_id>/', ClientDetails.as_view(),name='client-detail'),
    path('discussion/', QuestionsList.as_view(), name='discussion'),
    path('createquestion/', CreateQuestion.as_view(), name='create-question'),
    path('login/',
         auth_views.LoginView.as_view(template_name='knowledgebank/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='knowledgebank/logout.html'),
         name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='knowledgebank/password_reset.html'),
         name='password-reset'),
]

"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import verify_email, get_verification_results, get_verification_result, create_verification_result, update_verification_result, delete_verification_result
from django.views.generic import TemplateView

urlpatterns = [
    path('verify-email/', verify_email, name='verify_email'),
    path('verification-results/', get_verification_results, name='get_verification_results'),
    path('verification-results/<int:result_id>/', get_verification_result, name='get_verification_result'),
    path('create-verification-result/', create_verification_result, name='create_verification_result'),
    path('update-verification-result/<int:result_id>/', update_verification_result, name='update_verification_result'),
    path('delete-verification-result/<int:result_id>/', delete_verification_result, name='delete_verification_result'),
    path('verify-email-page/', TemplateView.as_view(template_name='verify_email.html'), name='verify_email_page'),
    path('view-results-page/', TemplateView.as_view(template_name='view_results.html'), name='view_results_page'),
]

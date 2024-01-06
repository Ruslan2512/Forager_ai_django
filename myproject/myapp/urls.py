from django.urls import path
from django.views.generic import TemplateView

from .views import verify_email, index

urlpatterns = [
    path('verify-email/', verify_email, name='verify_email'),
    path('verify-email-page/', TemplateView.as_view(template_name='verify_email.html'), name='verify_email_page'),
    path('view-results-page/', TemplateView.as_view(template_name='view_results.html'), name='view_results_page'),
    path('api/', index, name='index'),
]
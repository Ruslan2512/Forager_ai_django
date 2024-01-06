from django.urls import path
from .views import verify_email, get_verification_results, get_verification_result, create_verification_result, update_verification_result, delete_verification_result

urlpatterns = [
    path('verify-email/', verify_email, name='verify_email'),
    path('verification-results/', get_verification_results, name='get_verification_results'),
    path('verification-results/<int:result_id>/', get_verification_result, name='get_verification_result'),
    path('create-verification-result/', create_verification_result, name='create_verification_result'),
    path('update-verification-result/<int:result_id>/', update_verification_result, name='update_verification_result'),
    path('delete-verification-result/<int:result_id>/', delete_verification_result, name='delete_verification_result'),
]
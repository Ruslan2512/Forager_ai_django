from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .services import EmailVerificationService
from .models import EmailVerificationResult


@csrf_exempt
@require_POST
def verify_email(request):
    data = request.POST
    email = data.get('email', '')

    result = EmailVerificationService.verify_email(email)

    return JsonResponse({'email': result.email, 'is_valid': result.is_valid, 'verification_date': result.verification_date.strftime('%Y-%m-%d %H:%M:%S')})


@csrf_exempt
@require_GET
def get_verification_results(request):
    results = EmailVerificationResult.objects.all().values()
    return JsonResponse({'results': list(results)})


@csrf_exempt
@require_GET
def get_verification_result(request, result_id):
    try:
        result = EmailVerificationResult.objects.get(id=result_id)
        return JsonResponse({'email': result.email, 'is_valid': result.is_valid, 'verification_date': result.verification_date.strftime('%Y-%m-%d %H:%M:%S')})
    except EmailVerificationResult.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)


@csrf_exempt
@require_POST
def create_verification_result(request):
    data = request.POST
    email = data.get('email', '')

    result = EmailVerificationService.verify_email(email)

    return JsonResponse({'id': result.id, 'email': result.email, 'is_valid': result.is_valid, 'verification_date': result.verification_date.strftime('%Y-%m-%d %H:%M:%S')})


@csrf_exempt
@require_POST
def update_verification_result(request, result_id):
    try:
        result = EmailVerificationResult.objects.get(id=result_id)
    except EmailVerificationResult.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)

    data = request.POST
    email = data.get('email', '')

    result.email = email
    result.save()

    return JsonResponse({'id': result.id, 'email': result.email, 'is_valid': result.is_valid, 'verification_date': result.verification_date.strftime('%Y-%m-%d %H:%M:%S')})


@csrf_exempt
@require_POST
def delete_verification_result(request, result_id):
    try:
        result = EmailVerificationResult.objects.get(id=result_id)
    except EmailVerificationResult.DoesNotExist:
        return JsonResponse({'error': 'Result not found'}, status=404)

    result.delete()

    return JsonResponse({'message': 'Result deleted successfully'})

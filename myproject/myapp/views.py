from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .services import EmailVerificationService
from .models import EmailVerificationResult


data_storage = {'results': []}


@csrf_exempt
@require_POST
def verify_email(request):
    data = request.POST
    email = data.get('email', '')

    result = EmailVerificationService.verify_email(email)

    return JsonResponse({'email': result.email, 'is_valid': result.is_valid, 'verification_date': result.verification_date.strftime('%Y-%m-%d %H:%M:%S')})


def index(request):
    if request.method == 'GET':
        return JsonResponse(data_storage)

    elif request.method == 'POST':
        try:
            data = request.POST['data']
            data_storage['results'].append(data)
            return JsonResponse({'message': 'Text saved successfully'})
        except KeyError:
            return JsonResponse({'error': 'Invalid text format'})

    return JsonResponse({'error': 'Invalid request method'})

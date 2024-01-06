from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import EmailVerificationResult


class EmailVerificationService:
    @staticmethod
    def verify_email(email):
        try:
            validate_email(email)
            result = EmailVerificationResult(email=email, is_valid=True)
        except ValidationError:
            result = EmailVerificationResult(email=email, is_valid=False)

        result.save()
        return result

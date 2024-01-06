from django.db import models


class EmailVerificationResult(models.Model):
    email = models.EmailField()
    is_valid = models.BooleanField(default=False)
    verification_date = models.DateTimeField(auto_now_add=True)

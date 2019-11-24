from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Transfer(models.Model):
    IBAN_validator = RegexValidator(regex=r'^\d{26}$', message="Bank account number must have 26 digits.")

    sender = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)
    recipient_name = models.CharField(max_length=80, blank=False, null=False)
    recipient_account = models.CharField(validators=[IBAN_validator], null=False, max_length=26)
    title = models.CharField(max_length=60, blank=False, null=False)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    date = models.DateField(auto_now_add=True)

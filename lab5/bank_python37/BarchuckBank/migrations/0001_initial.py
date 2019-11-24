# Generated by Django 2.2.7 on 2019-11-24 11:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=80)),
                ('recipient_account', models.CharField(max_length=26, validators=[django.core.validators.RegexValidator(message='Bank registration must have 26 digits.', regex='^\\d{26}$')])),
                ('title', models.CharField(max_length=60)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=22)),
                ('date', models.DateField(auto_now_add=True)),
                ('sender', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

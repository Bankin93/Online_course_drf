# Generated by Django 4.2.2 on 2023-07-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0010_payments_payment_intent_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='confirmation',
            field=models.BooleanField(default=False, verbose_name='подтверждение платежа'),
        ),
    ]

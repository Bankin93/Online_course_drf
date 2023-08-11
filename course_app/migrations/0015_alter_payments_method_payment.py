# Generated by Django 4.2.2 on 2023-07-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0014_course_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='method_payment',
            field=models.CharField(choices=[('cash', 'наличные'), ('transfer', 'перевод')], default='transfer', max_length=20, verbose_name='способ оплаты'),
        ),
    ]

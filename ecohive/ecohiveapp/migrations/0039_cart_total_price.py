# Generated by Django 4.2.4 on 2023-09-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohiveapp', '0038_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

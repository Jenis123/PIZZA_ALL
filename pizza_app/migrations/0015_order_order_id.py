# Generated by Django 4.0.5 on 2022-07-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0014_alter_mycart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0007_alter_menu_pizza_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='pizza_image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
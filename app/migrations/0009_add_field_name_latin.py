# Generated by Django 3.2.8 on 2021-11-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_user_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_latin',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 3.2.8 on 2022-01-06 09:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_Add_CkEditor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images_list',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]

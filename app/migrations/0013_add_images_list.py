from django.db import migrations
from rest_framework.utils import json

from app.utils.constants import USER_ROLE
from server.settings import BASE_DIR


def get_category_thumbnail(category_name):
    data = {
        'Laptop': 'fas fa-laptop',
        "Bàn phím": "fas fa-keyboard",
        "Chuột": "fas fa-mouse",
        "Tai nghe": "fas fa-headphones",
        "Tay cầm chơi game": "fab fa-xbox",
        "PC": "fas fa-hdd",
        "Màn hình": "fas fa-desktop",
        "Ghế Gaming": "fas fa-chair",
    }
    return data[category_name]


def create_data(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Product = apps.get_model('app', 'Product')
    product_list = Product.objects.all()
    for product in product_list:
        images = product.images.all()
        data = ''
        for e in images:
            data += f'<p><img alt="" src="{e.url}"/></p>'
        product.images_list = data
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_add_images_list_field'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

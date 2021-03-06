from django.db import migrations
from rest_framework.utils import json

from server.settings import BASE_DIR


def get_category_thumbnail(category_name):
    data = {
        'laptop': 'fas fa-laptop',
        "bàn phím": "fas fa-keyboard",
        "chuột": "fas fa-mouse",
        'chuột máy tính': 'fas fa-mouse',
        "tai nghe": "fas fa-headphones",
        "tay cầm chơi game": "fab fa-xbox",
        "pc": "fas fa-hdd",
        "màn hình": "fas fa-desktop",
        "ghế gaming": "fas fa-chair",
        'pc linh kiện': 'fas fa-hdd',
        'tivi': 'fas fa-desktop',
        'thiết bị thông minh': 'fas fa-camera',
        'điện thoại & tablet': 'fas fa-mobile-alt'

    }
    return data.get(category_name.lower(), '')


def create_data(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Product = apps.get_model('app', 'Product')
    Category = apps.get_model('app', 'Category')
    Brand = apps.get_model('app', 'Brand')
    Image = apps.get_model('app', 'Image')
    with open(BASE_DIR / 'init_data3.json', encoding='utf-8') as f:
        json_data = f.read()
    # print(json_data)
    json_data = json.loads(json_data)
    for product in json_data:
        try:
            m_brand = Brand.objects.get(name=product['brand'])
        except Brand.DoesNotExist:
            m_brand = Brand.objects.create(
                name=product['brand']
            )
            m_brand.save()

        if '/' in product['category']:
            product['category'] = product['category'].split('/')[1]
        try:
            m_category = Category.objects.get(name=product['category'])
        except Category.DoesNotExist:
            m_category = Category.objects.create(
                name=product['category'],
                thumbnail=get_category_thumbnail(product['category'])
            )
            m_category.save()

        m_category.brands.add(m_brand)
        m_category.save()

        # images
        m_images = []
        for e in product['images']:
            c_image = Image.objects.create(
                url=e['url'],
                label=e['label']
            )
            c_image.save()
            m_images.append(c_image)

        m_product = Product.objects.create(
            id=product['id'],
            name=product['name'],
            thumbnail=product['thumbnail'],
            brand=m_brand,
            price=product['price'],
            sale_price=product['sale_price'],
            category =m_category,
            specifications=product['specifications'],
            short_description=product['short_description'],
            description=product['description'],
        )
        m_product.images.set(m_images)
        m_product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

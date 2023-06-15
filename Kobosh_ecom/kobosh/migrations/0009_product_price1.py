# Generated by Django 4.2.1 on 2023-06-06 12:38

from django.db import migrations
import kobosh.models


class Migration(migrations.Migration):

    dependencies = [
        ('kobosh', '0008_rename_image3_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price1',
            field=kobosh.models.CommaSeparatedIntegerField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

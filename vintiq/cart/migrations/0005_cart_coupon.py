# Generated by Django 4.2.4 on 2023-09-19 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_coupon'),
        ('cart', '0004_alter_cart_item_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.coupon'),
        ),
    ]

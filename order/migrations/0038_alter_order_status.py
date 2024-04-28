# Generated by Django 4.2.11 on 2024-04-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0037_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Cancelled', 'Cancelled'), ('Order confirmed', 'Order confirmed'), ('Delivered', 'Delivered'), ('Return requested', 'Return requested'), ('Return processing', 'Return processing'), ('Returned', 'Returned'), ('Shipped', 'Shipped')], default='Order confirmed', max_length=50),
        ),
    ]

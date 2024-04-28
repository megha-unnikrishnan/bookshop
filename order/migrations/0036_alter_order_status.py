# Generated by Django 4.2.11 on 2024-04-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0035_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned'), ('Out for delivery', 'Out for delivery'), ('Return processing', 'Return processing'), ('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Return requested', 'Return requested')], default='Order confirmed', max_length=50),
        ),
    ]

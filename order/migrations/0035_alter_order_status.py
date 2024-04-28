# Generated by Django 4.2.11 on 2024-04-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Return processing', 'Return processing'), ('Cancelled', 'Cancelled'), ('Shipped', 'Shipped'), ('Returned', 'Returned'), ('Order confirmed', 'Order confirmed'), ('Return requested', 'Return requested')], default='Order confirmed', max_length=50),
        ),
    ]

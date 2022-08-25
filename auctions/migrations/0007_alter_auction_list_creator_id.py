# Generated by Django 4.1 on 2022-08-22 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_auction_list_category_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='creator_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]

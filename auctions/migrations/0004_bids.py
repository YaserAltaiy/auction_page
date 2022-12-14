# Generated by Django 4.1 on 2022-08-22 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('user_time_bid', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='auctions.auction_list')),
                ('user_bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

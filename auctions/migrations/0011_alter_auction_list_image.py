# Generated by Django 4.1 on 2022-08-24 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auction_list_category_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='image',
            field=models.URLField(default='https://i.pinimg.com/736x/01/7c/44/017c44c97a38c1c4999681e28c39271d.jpg'),
        ),
    ]

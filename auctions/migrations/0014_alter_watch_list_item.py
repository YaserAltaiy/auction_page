# Generated by Django 4.1 on 2022-08-25 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_rename_comments_comment_watch_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch_list',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='auctions.auction_list', unique=True),
        ),
    ]
# Generated by Django 4.1 on 2022-08-24 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_auction_list_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_time', models.DateTimeField()),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auctions.auction_list')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='comment',
        ),
    ]

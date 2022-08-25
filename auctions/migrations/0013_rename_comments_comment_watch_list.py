# Generated by Django 4.1 on 2022-08-24 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_comments_delete_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.CreateModel(
            name='Watch_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='auctions.auction_list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
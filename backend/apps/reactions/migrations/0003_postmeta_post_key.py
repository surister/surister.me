# Generated by Django 4.0.3 on 2022-03-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0002_alter_postmeta_reactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmeta',
            name='post_key',
            field=models.CharField(default='yest', max_length=128),
            preserve_default=False,
        ),
    ]
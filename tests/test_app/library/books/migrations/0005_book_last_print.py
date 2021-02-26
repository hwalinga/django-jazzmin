# Generated by Django 2.2.16 on 2021-02-26 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='last_print',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
            preserve_default=False,
        ),
    ]
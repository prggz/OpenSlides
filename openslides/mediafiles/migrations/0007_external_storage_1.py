# Generated by Django 2.2.8 on 2019-12-11 14:11

import jsonfield.encoder
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mediafiles", "0006_directories_and_permissions_3"),
    ]

    operations = [
        migrations.AddField(
            model_name="mediafile",
            name="filesize",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="mediafile",
            name="mimetype",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="mediafile",
            name="pdf_information",
            field=jsonfield.fields.JSONField(
                default=dict,
                dump_kwargs={
                    "cls": jsonfield.encoder.JSONEncoder,
                    "separators": (",", ":"),
                },
                load_kwargs={},
            ),
        ),
    ]

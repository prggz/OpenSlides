# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 10:58
from __future__ import unicode_literals

from django.db import migrations

from openslides.utils.migrations import (
    add_permission_to_groups_based_on_existing_permission,
)


class Migration(migrations.Migration):

    dependencies = [("core", "0004_auto_20170215_1624")]

    operations = [
        migrations.AlterModelOptions(
            name="configstore",
            options={
                "default_permissions": (),
                "permissions": (
                    ("can_manage_config", "Can manage configuration"),
                    ("can_manage_logos", "Can manage logos"),
                ),
            },
        ),
        migrations.RunPython(
            add_permission_to_groups_based_on_existing_permission(
                "can_manage_config",
                "configstore",
                "core",
                "can_manage_logos",
                "Can manage logos",
            )
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-16 16:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_persona_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='resume',
            field=ckeditor.fields.RichTextField(default='Empty'),
            preserve_default=False,
        ),
    ]

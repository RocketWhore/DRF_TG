# Generated by Django 4.2.4 on 2023-08-24 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_conn', '0005_alter_processedmessage_message_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConnectedChats',
        ),
    ]

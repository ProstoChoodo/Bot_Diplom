# Generated by Django 5.0 on 2024-04-13 11:18

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PromptVariable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('prompt', models.CharField(default='1girl', max_length=100, null=True)),
                ('batch_size', models.BigIntegerField(default=1)),
                ('width', models.BigIntegerField(default=480)),
                ('height', models.BigIntegerField(default=800)),
                ('enable_hr', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='bot.user')),
            ],
        ),
    ]
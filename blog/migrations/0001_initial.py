# Generated by Django 4.0.1 on 2022-02-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('keyword', models.TextField(blank=True)),
                ('describe', models.TextField(blank=True)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('Timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]

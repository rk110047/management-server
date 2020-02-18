# Generated by Django 3.0 on 2020-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page_url', models.URLField()),
                ('site_title', models.CharField(blank=True, max_length=255, null=True)),
                ('site_description', models.TextField(blank=True, null=True)),
                ('site_logo', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Home Settings',
            },
        ),
    ]
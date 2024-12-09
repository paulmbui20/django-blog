# Generated by Django 5.1.4 on 2024-12-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_blogpost_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_path', models.CharField(max_length=255)),
                ('sessions', models.IntegerField()),
                ('pageviews', models.IntegerField()),
                ('absolute_url', models.URLField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

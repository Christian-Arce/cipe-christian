# Generated by Django 2.2.8 on 2020-01-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200109_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scientist',
            name='academia_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='facebook_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='gscholar_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='institutional_website',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='linkedin_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='orcid_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='personal_website',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='researchgate_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='scopus_profile',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='twitter_handler',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]

# Generated by Django 2.2.24 on 2021-06-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_historicalorganizationcourse'),
        ('course_creators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecreator',
            name='all_organizations',
            field=models.BooleanField(default=True, help_text='Grant the user the permission to create courses in ALL organizations'),
        ),
        migrations.AddField(
            model_name='coursecreator',
            name='organizations',
            field=models.ManyToManyField(blank=True, help_text='Organizations under which the user is allowed to create courses.', to='organizations.Organization'),
        ),
    ]

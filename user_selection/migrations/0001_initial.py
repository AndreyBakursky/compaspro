# Generated by Django 4.0.6 on 2022-07-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('RT', 'Root'), ('MR', 'Manager'), ('CA', 'CRM-administrator')], default='RT', max_length=2)),
                ('offer', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, upload_to='photos/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

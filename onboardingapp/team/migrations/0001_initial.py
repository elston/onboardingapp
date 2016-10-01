# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-01 12:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_temp', models.BooleanField(default=False)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('last4_card_num', models.CharField(blank=True, max_length=4, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('subscription_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('org_limit', models.IntegerField(default=0)),
                ('team_limit', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('stripe_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Toggl', 'Toggl'), ('Github', 'Github'), ('Jira', 'Jira'), ('Asana', 'Asana'), ('Bitbucket', 'Bitbucket'), ('Trello', 'Trello'), ('Zendesk', 'Zendesk'), ('Quay', 'Quay'), ('Box', 'Box'), ('HipChat', 'HipChat'), ('__pycache__', '__pycache__'), ('Dropbox', 'Dropbox'), ('Slack', 'Slack')], max_length=50)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('org_name', models.CharField(blank=True, max_length=200, null=True)),
                ('team_name', models.CharField(blank=True, max_length=200, null=True)),
                ('team_id', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1024)),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.ManyToManyField(related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(blank=True, related_name='team_member', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('service', models.ManyToManyField(blank=True, related_name='team_service', to='team.Service')),
            ],
        ),
        migrations.AddField(
            model_name='errorlog',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='team.Service'),
        ),
        migrations.AddField(
            model_name='errorlog',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='team.Team'),
        ),
        migrations.AddField(
            model_name='errorlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_info', to='team.Service'),
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_info', to='team.Team'),
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamuser_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teamuser',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to='team.Account'),
        ),
        migrations.AddField(
            model_name='teamuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='teamuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]

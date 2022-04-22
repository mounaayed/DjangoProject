# Generated by Django 4.0.1 on 2022-02-07 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('needs', models.TextField(max_length=250)),
                ('timeallocated', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('Isvalid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hub.user')),
            ],
            bases=('hub.user',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hub.user')),
            ],
            bases=('hub.user',),
        ),
        migrations.CreateModel(
            name='MembershipProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated_by_member', models.IntegerField()),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.student')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='Supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_sup', to='hub.supervisor'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hub.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='lesmembers', through='hub.MembershipProject', to='hub.Student'),
        ),
    ]
# Generated by Django 3.2 on 2022-07-10 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_alter_admin_new_depart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='姓名')),
            ],
        ),
        migrations.CreateModel(
            name='B2G',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=32, verbose_name='地点')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.boy')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.girl')),
            ],
        ),
    ]

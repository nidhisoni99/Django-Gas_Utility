# Generated by Django 4.2.4 on 2023-08-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20)),
                ('service_type', models.CharField(choices=[('gas_leak', 'Gas Leak'), ('gas_supply', 'Gas Supply Issue'), ('maintenance', 'Maintenance Request')], max_length=20)),
                ('details', models.TextField()),
                ('attachment', models.FileField(blank=True, upload_to='service_attachments/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

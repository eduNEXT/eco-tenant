# Generated by Django 2.2.16 on 2020-10-22 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('edunext', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteOptions',
            new_name='TenantOptions',
        ),
        migrations.AlterModelOptions(
            name='tenantoptions',
            options={'verbose_name_plural': 'TenantOptions'},
        ),
    ]
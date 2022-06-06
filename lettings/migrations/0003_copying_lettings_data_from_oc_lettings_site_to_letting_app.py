# Generated by Django 3.0 on 2022-06-06 18:38

from django.apps import apps as global_apps
from django.db import migrations


def forwards(apps, schema_editor):
    try:
        letting_old = apps.get_model('oc_lettings_site', 'letting')
    except LookupError:
        # The old app isn't installed.
        return

    letting_new = apps.get_model('lettings', 'letting')

    for old_object in letting_old.objects.all():
        letting_dict = old_object.__dict__
        del letting_dict['_state']
        del letting_dict['id']

        # letting_new.objects.bulk_creat
        letting_new.objects.create(**letting_dict)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_copying_letting_data_from_oc_lettings_site_to_letting_app'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]

    if global_apps.is_installed('oc_lettings_site'):
        dependencies.append(('oc_lettings_site', '0001_initial'))

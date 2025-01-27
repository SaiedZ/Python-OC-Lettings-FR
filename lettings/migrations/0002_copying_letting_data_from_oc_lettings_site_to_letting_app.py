# Generated by Django 3.0 on 2022-06-06 18:24

from django.apps import apps as global_apps
from django.db import migrations


def forwards(apps, schema_editor):
    try:
        address_old = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        # The old app isn't installed.
        return

    address_new = apps.get_model('lettings', 'Address')

    for old_object in address_old.objects.all():
        adress_dict = old_object.__dict__
        del adress_dict['_state']
        del adress_dict['id']

        # address_new.objects.bulk_creat
        address_new.objects.create(**adress_dict)
        address_new


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_model_creation'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]

    if global_apps.is_installed('oc_lettings_site'):
        dependencies.append(('oc_lettings_site', '0001_initial'))

from django.db import migrations
from django.contrib.auth.models import Group

def create_groups(apps, schema_editor):
    Group.objects.create(name='Admin')
    Group.objects.create(name='User')

class Migration(migrations.Migration):

    dependencies = [
        ('Book_Rat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]

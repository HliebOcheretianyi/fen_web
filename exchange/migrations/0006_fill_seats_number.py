import re

from django.db import migrations


def fill_seats_number(apps, schema_editor):
    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        match = re.search(r'\d+', program.seats)
        program.seats_num = int(match.group()) if match else 0
        program.save(update_fields=['seats_num'])


def restore_seats_text(apps, schema_editor):
    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        program.seats = str(program.seats_num)
        program.save(update_fields=['seats'])


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_add_seats_number'),
    ]

    operations = [
        migrations.RunPython(fill_seats_number, reverse_code=restore_seats_text),
    ]
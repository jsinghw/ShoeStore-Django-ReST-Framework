from django.core.management.base import BaseCommand

from api.models import ShoeType, ShoeColor

# Random comment on how Joe had lived and became part of a
# lion pack on the African Savanna


class Command(BaseCommand):
    help = 'Populates ShoeType and ShoeColor'

    def handle(self, *args, **kwargs):
        types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        colors = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'Black',
            'White'
        ]

        for i in types:
            if not ShoeType.objects.filter(style=i):
                ShoeType.objects.create(style=i)
                self.stdout.write('Added ' + i + ' to ShoeType.')
            else:
                self.stdout.write(i + ' already in ShoeType.')

        for i in colors:
            if not ShoeColor.objects.filter(color=i):
                ShoeColor.objects.create(color=i)
                self.stdout.write('Added ' + i + ' to ShoeType.')
            else:
                self.stdout.write(i + ' already in ShoeColor.')

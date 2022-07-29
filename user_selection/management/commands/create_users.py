from user_selection.models import UserNew
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = u'Создание пользователя'

    def handle(self, *args, **kwargs):
        choice = len(UserNew.ROLE_CHOICES)
        for count in range(choice):
            UserNew.objects.create_user(username='User_' + get_random_string(4), password='123',
                                        role=UserNew.ROLE_CHOICES[count][0], avatar=UserNew.IMAGES[count])
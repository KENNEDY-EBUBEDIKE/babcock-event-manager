from .models import User
from apps.scheduler.models import Venue


def seed_data(sender, **kwargs):
    # Create some records for MyModel
    try:
        new_user = User.objects.create_superuser(
            email='admin@email.com',
            username='admin',
            password='admin',

        )
        new_user.first_name = 'IT'
        new_user.surname = 'ADMINISTRATOR'
        new_user.department = 'ICT'
        new_user.save()
    except Exception as e:
        print(e)
        pass

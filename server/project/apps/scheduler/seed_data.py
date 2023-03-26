from .models import Venue


def seed_data(sender, **kwargs):
    try:
        new_venue = Venue.objects.create(
            name='BUCODEL LAB 1',
            capacity=155,
            coordinate='6.892166734971729, 3.718272489395086',
        )
        new_venue.features = {
            'Electronic Board': 1,
            'Standing Fan': 1,
            "Inverter": 1,
            "Desktops and Seats": 147,
        }
        new_venue.save()
    except Exception as e:
        print(e)
        pass

    try:
        new_venue = Venue.objects.create(
            name='BUCODEL LAB 2',
            capacity=171,
            coordinate='6.892166734971729, 3.718272489395086',
        )
        new_venue.features = {
            'Electronic Board': 1,
            'Standing AC': 1,
            "Inverter": 1,
            "Desktops and Seats": 159,
        }
        new_venue.save()
    except Exception as e:
        print(e)
        pass

    try:
        new_venue = Venue.objects.create(
            name='BUCODEL LAB 3',
            capacity=350,
            coordinate='6.892166734971729, 3.718272489395086',
        )
        new_venue.features = {
            'Electronic Board': 1,
            'Fans': 6,
            "Inverter": 1,
            "Seats and Tables": 216,
        }
        new_venue.save()
    except Exception as e:
        print(e)
        pass

    try:
        new_venue = Venue.objects.create(
            name='BUCODEL LAB 4',
            capacity=184,
            coordinate='6.892166734971729, 3.718272489395086',
        )
        new_venue.features = {
            'White Board': 1,
            'Fans': 6,
            "Seats and Tables": 196,
        }
        new_venue.save()
    except Exception as e:
        print(e)
        pass

    try:
        new_venue = Venue.objects.create(
            name='BUCODEL LAB 5',
            capacity=318,
            coordinate='6.892166734971729, 3.718272489395086',
        )
        new_venue.features = {
            'Electronic Board': 1,
            'Fans': 5,
            "Inverter": 1,
            "Seats and Tables": 184,
        }
        new_venue.save()
    except Exception as e:
        print(e)
        pass

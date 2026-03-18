import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
django.setup()

from myapp.models import Team, Driver, Track
from datetime import date

def seed_database():
    print("Seeding F1 Database...")
    
    # 1. Teams
    teams_data = [
        {"name": "Mercedes", "principal": "Toto Wolff", "engine_supplier": "Mercedes"},
        {"name": "Red Bull Racing", "principal": "Christian Horner", "engine_supplier": "Honda RBPT"},
        {"name": "Ferrari", "principal": "Frederic Vasseur", "engine_supplier": "Ferrari"},
        {"name": "McLaren", "principal": "Andrea Stella", "engine_supplier": "Mercedes"},
        {"name": "Aston Martin", "principal": "Mike Krack", "engine_supplier": "Mercedes"},
    ]
    
    teams = {}
    for t_data in teams_data:
        team, created = Team.objects.get_or_create(name=t_data['name'], defaults=t_data)
        teams[t_data['name']] = team

    # 2. Drivers (2025/2026 Expected Lineups roughly)
    drivers_data = [
        {"name": "Max Verstappen", "team_name": "Red Bull Racing", "nationality": "Dutch", "points": 0, "wins": 61, "podiums": 105},
        {"name": "Sergio Perez", "team_name": "Red Bull Racing", "nationality": "Mexican", "points": 0, "wins": 6, "podiums": 39},
        {"name": "Lewis Hamilton", "team_name": "Ferrari", "nationality": "British", "points": 0, "wins": 105, "podiums": 197},
        {"name": "Charles Leclerc", "team_name": "Ferrari", "nationality": "Monegasque", "points": 0, "wins": 6, "podiums": 35},
        {"name": "Lando Norris", "team_name": "McLaren", "nationality": "British", "points": 0, "wins": 1, "podiums": 18},
        {"name": "Oscar Piastri", "team_name": "McLaren", "nationality": "Australian", "points": 0, "wins": 0, "podiums": 3},
        {"name": "George Russell", "team_name": "Mercedes", "nationality": "British", "points": 0, "wins": 1, "podiums": 12},
        {"name": "Andrea Kimi Antonelli", "team_name": "Mercedes", "nationality": "Italian", "points": 0, "wins": 0, "podiums": 0},
        {"name": "Fernando Alonso", "team_name": "Aston Martin", "nationality": "Spanish", "points": 0, "wins": 32, "podiums": 106},
    ]

    for d_data in drivers_data:
        team_obj = teams[d_data.pop('team_name')]
        d_data['team'] = team_obj
        Driver.objects.get_or_create(name=d_data['name'], defaults=d_data)

    # 3. Tracks (2026 Schedule preview)
    tracks_data = [
        {"name": "Bahrain Grand Prix", "location": "Sakhir", "length_km": 5.412, "laps": 57, "race_date": date(2026, 3, 1)},
        {"name": "Saudi Arabian Grand Prix", "location": "Jeddah", "length_km": 6.174, "laps": 50, "race_date": date(2026, 3, 15)},
        {"name": "Australian Grand Prix", "location": "Melbourne", "length_km": 5.278, "laps": 58, "race_date": date(2026, 3, 29)},
        {"name": "Japanese Grand Prix", "location": "Suzuka", "length_km": 5.807, "laps": 53, "race_date": date(2026, 4, 12)},
        {"name": "Chinese Grand Prix", "location": "Shanghai", "length_km": 5.451, "laps": 56, "race_date": date(2026, 4, 26)},
        {"name": "Miami Grand Prix", "location": "Miami", "length_km": 5.412, "laps": 57, "race_date": date(2026, 5, 10)},
        {"name": "Emilia Romagna GP", "location": "Imola", "length_km": 4.909, "laps": 63, "race_date": date(2026, 5, 24)},
        {"name": "Monaco Grand Prix", "location": "Monte Carlo", "length_km": 3.337, "laps": 78, "race_date": date(2026, 6, 7)},
        {"name": "Canadian Grand Prix", "location": "Montreal", "length_km": 4.361, "laps": 70, "race_date": date(2026, 6, 21)},
        {"name": "British Grand Prix", "location": "Silverstone", "length_km": 5.891, "laps": 52, "race_date": date(2026, 7, 5)},
    ]

    for tr_data in tracks_data:
        Track.objects.get_or_create(name=tr_data['name'], defaults=tr_data)

    print("Success! Database seeded with 5 Teams, 9 Drivers, and 10 Tracks.")

if __name__ == '__main__':
    seed_database()

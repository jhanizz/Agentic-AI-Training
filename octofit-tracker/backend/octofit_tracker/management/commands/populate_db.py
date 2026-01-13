from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc.name)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc.name)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=batman, type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=superman, type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user=captain, type='walk', duration=20, date='2023-01-04')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do 30 situps', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='hard')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100, rank=1)
        Leaderboard.objects.create(user=batman, score=90, rank=2)
        Leaderboard.objects.create(user=superman, score=80, rank=3)
        Leaderboard.objects.create(user=captain, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))

from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    engine_supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers')
    nationality = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length_km = models.FloatField()
    laps = models.IntegerField()
    race_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['race_date']

    def __str__(self):
        return f"{self.name} - {self.race_date.strftime('%b %d, %Y') if self.race_date else 'TBD'}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)]) # 1 to 10
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'driver') # A user can only rate a driver once

    def __str__(self):
        return f"{self.user.username}'s {self.score}/10 for {self.driver.name}"

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'track') # A user can only make one prediction per track

    def __str__(self):
        return f"{self.user.username} predicts {self.driver.name} wins at {self.track.name}"

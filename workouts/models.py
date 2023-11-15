from django.db import models
from users.models import User

class Exercise(models.Model):
    MUSCULAR_GROUPS = [
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('legs', 'Legs'),
        ('shoulders', 'Shoulders'),
        ('arms', 'Arms'),
        ('core', 'Core'),
    ]
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=20, choices=MUSCULAR_GROUPS)
    tutorial = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=50)
    date = models.DateField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return self.title

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    weights = models.DecimalField(max_digits=5,decimal_places=2)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.workout.title} - {self.exercise.name}'


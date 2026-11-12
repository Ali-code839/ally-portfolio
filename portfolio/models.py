# Import Django's database model tools.
from django.db import models


# Define the database model representing one portfolio project.
class Project(models.Model):
    # Store the available project categories as database-friendly values and readable labels.
    CATEGORY_CHOICES = [
        ('graphic', 'Graphic Design'),
        ('photo', 'Photography'),
        ('video', 'Videography'),
        ('web', 'Web Development'),
    ]

    # Store the public project title.
    title = models.CharField(max_length=200)

    # Store the project description shown below the project image.
    description = models.TextField()

    # Store the project's uploaded image inside media/projects/.
    image = models.ImageField(upload_to='projects/', blank=True)

    # Store the selected category for filtering projects on the portfolio page.
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    # Store when the project was created so recent work can appear first.
    created_at = models.DateTimeField(auto_now_add=True)

    # Return the project title whenever Django needs a human-readable project name.
    def __str__(self):
        return self.title

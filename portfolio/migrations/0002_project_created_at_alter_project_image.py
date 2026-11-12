# Import Django migration and model helpers.
from django.db import migrations, models
from django.utils import timezone


# Define the database changes needed by the upgraded Project model.
class Migration(migrations.Migration):
    # Depend on the original Project migration.
    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    # Apply the new fields and image setting to the Project table.
    operations = [
        # Add a creation timestamp to existing and future projects.
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
        ),
        # Allow projects without an uploaded image so placeholder cards can still work.
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
        # Remove the temporary null setting from created_at after existing rows receive a value.
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

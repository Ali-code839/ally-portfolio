# Import Django migration and model helpers.
from django.db import migrations, models


# Define the database changes needed by the upgraded Project model.
class Migration(migrations.Migration):

    # Depend on the original Project migration.
    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    # Update the image field only.
    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
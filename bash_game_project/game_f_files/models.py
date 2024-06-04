import os
import shutil
import tempfile
import zipfile
from django.db import models
from django.conf import settings


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    game_file = models.FileField(upload_to='games/')  # Upload zip file containing the game
    unzipped_location = models.CharField(max_length=255, blank=True, null=True)
    #<script src="{{ game.unzipped_location }}/main.js"></script>

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        

    def delete(self, *args, **kwargs):
        # Get the path where the game files are extracted
        extract_path = os.path.join(settings.MEDIA_ROOT, 'games', str(self.pk))
        # Remove the extracted files if they exist
        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)
        # Remove the uploaded zip file if it exists
        if self.game_file:
            self.game_file.delete(save=False)
        # Call the superclass method to delete the database record
        super().delete(*args, **kwargs)

    def unzip_file(self):
        if not self.game_file:
            return

        # Create a temporary file to hold the uploaded zip file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in self.game_file.chunks():
                tmp_file.write(chunk)
            tmp_file_path = tmp_file.name

        try:
            if zipfile.is_zipfile(tmp_file_path):
                with zipfile.ZipFile(tmp_file_path, 'r') as zip_ref:
                    extract_path = os.path.join(settings.MEDIA_ROOT, 'games', str(self.pk))
                    zip_ref.extractall(extract_path)
                    self.unzipped_location = os.path.join(settings.MEDIA_URL, 'games', str(self.pk)).replace("\\", "/")
                    self.save(update_fields=['unzipped_location'])  # Save the unzipped location
        finally:
            # Delete the temporary file
            os.remove(tmp_file_path)

        # Delete the original uploaded file
        self.game_file.delete()

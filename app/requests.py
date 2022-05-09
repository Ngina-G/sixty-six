from .models import Pitch

def create_pitches(id,category,pitch,pitch_author):
    """function t create pitch
    """
    new_pitch = Pitch(id, category, pitch, pitch_author)
    return new_pitch

def save_pitch(pitch):
    """Function to save pitches
    """
    return pitch.save_pitch()

def delete_pitch(pitch):
    """Function to delete pitch
    """
    pitch.clear_pitch()

def get_pitch(category):
    """function to find a pitch by category
    """
    return Pitch.get_pitches(category)

def get_all_pitches(self):
    """function to return all pitches
    """
    return self.all_pitches
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

def find_pitch(category):
    """function to find a pitch by category
    """
    return Pitch.search_pitches(category)

def display_all_pitches(self):
    """function to return all pitches
    """
    return self.all_pitches

def get_pitch(id):
    pitch_object = None
    if pitch_details:
        id = Pitch.id
        category = Pitch.category
        pitch = Pitch.pitch
        pitch_author = Pitch.pitch_author
        
        pitch_object = Pitch(id, category, pitch, pitch_author)
    return pitch_object
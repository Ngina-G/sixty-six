import unittest
from app.models import Pitch
from app import db

class PitchTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.new_pitch = Pitch( 'Business', 'Businesses fail all the time', 'John Doe')

    def test_initialization(self):
        self.assertEquals(self.new_pitch.pitch, 'Businesses fail all the time')
        self.assertEquals(self.new_pitch.pitch_author, 'John Doe')
        self.assertEquals(self.new_pitch.category, 'Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

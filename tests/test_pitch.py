import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.new_pitch= Pitch(1, 'Business', 'Businesses fail all the time', 'John Doe')

    def test_initialization(self):
        self.assertEqual(self.new_pitch.id, 1)
        self.assertEqual(self.new_pitch.category, 'Business')
        self.assertEqual(self.new_pitch.pitch, 'Businesses fail all the time')
        self.assertEqual(self.new_pitch.pitch_author, 'John Doe')

    def tearDown(self):
        Pitch.clear_pitch()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.all_pitches)>0)


    def test_get_pitch_by_category(self):
        
        self.new_pitch.save_pitch()
        test_pitch= Pitch(1, 'Business', 'Businesses fail all the time', 'John Doe')
        test_pitch.save_pitch()

        got_pitch = Pitch.search_pitches('Business')
        self.assertEqual(got_pitch.pitch, test_pitch.pitch)
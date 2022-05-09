import unittest
from app.models import Comment
# Comment = comment.Comment

class CommentTest(unittest.TestCase):
    """
        Test class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
            Set up method that will run before every test
        """
        self.new_comment= Comment(1, 'Consistency is key', 'Jane Doe')

    def test_initialization(self):
        self.assertEqual(self.new_comment.pitch_id, 1)
        self.assertEqual(self.new_comment.content, 'Consistency is key')
        self.assertEqual(self.new_comment.author, 'Jane Doe')

    def tearDown(self):
        Comment.clear_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.all_comments)>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1)
        self.assertTrue(len(got_comments) == 1)
import unittest
from models.album import album

class Testalbum(unittest.TestCase):
    
    def setUp(self):
        self.album = album("Walk Dog", "Ada Lovelace", 60)
    
    
    def test_album_has_title(self):
        self.assertEqual("Walk Dog", self.album.title)
        
        
    def test_album_has_assignee(self):
        self.assertEqual("Ada Lovelace", self.album.assignee)
       
        
    def test_album_has_genre(self):
        self.assertEqual(60, self.album.genre)
    
    
    def test_album__starts_false(self):
        self.assertEqual(False, self.album.)
        
    
    def test_can_mark_test_complete(self):
        self.album.mark_complete()
        self.assertEqual(True, self.album.)
    
    
   
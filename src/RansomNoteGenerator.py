class RansomNoteGenerator(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_note_chars = [ch for ch in ransomNote]
        magazine_chars = [ch for ch in magazine]
        while len(ransom_note_chars) > 0:
            ch = ransom_note_chars[0]
            if ch in magazine_chars:
                magazine_chars.remove(ch)
                ransom_note_chars.remove(ch)
            else:
                return False
            if len(magazine_chars) == 0 and len(ransom_note_chars) > 0:
                return False
        return True    

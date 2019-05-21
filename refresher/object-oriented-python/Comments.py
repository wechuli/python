

class Comment:
    def __init__(self, username, text, likes=0):
        self._username = username
        self._text = text
        self._likes = likes

    def get_data(self):
        return [self._username, self._text, self._likes]


comment = Comment('Wechuli',"So funny, ha ha")
print(comment.get_data())
print(dir(Comment))

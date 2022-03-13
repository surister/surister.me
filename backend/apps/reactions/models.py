from enum import Enum

from django.db import models


class PostMeta(models.Model):
    class Emoji(Enum):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4

    """
    Reactions will be stored as an integer, 0000_0000_0000_0000
                                              4    3    2    1    emoji_id
                                              
                                              
    This awful but fun implementation assumes that we are only going to be using 4 emojis and the max
    numbers of emoji's upvote is 9999.
    
    
    """
    reactions = models.IntegerField(default=0)

    def add_emoji(self, emoji_id: int) -> None:
        """
        The sum below maps value to place in the integer.
        so value 4 will sum 10*12
        :param emoji_id:
        :return:
        """
        self.reactions += 10 ** (4 * (int(emoji_id) - 1))
        self.save()

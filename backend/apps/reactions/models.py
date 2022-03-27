from enum import Enum

from django.db import models
from rest_framework.exceptions import ValidationError


class PostMeta(models.Model):
    class Emoji(Enum):
        # For SQLITE integer max is reached at 6 Emojis.
        # Perhaps we should use a real implementation (It'd be boring)
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
    post_key = models.CharField(max_length=128)

    def add_emoji(self, emoji_id: int) -> None:
        """
        The sum below maps value to place in the integer.
        so value 4 will sum 10*12
        :param emoji_id:
        :return:
        """
        if 0 > emoji_id or emoji_id > len(PostMeta.Emoji):
            raise ValidationError(f'Emoji values should be between 1 to {len(PostMeta.Emoji)}')

        self.reactions += 10 ** (len(PostMeta.Emoji) * (int(emoji_id) - 1))
        self.save()

    def emoji_to_json(self):
        pass
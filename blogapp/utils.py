from .models import Blog, Tag
from typing import List


class TagUtils:
    '''
    Class to handle hashtags in blogposts while adding a new blog-post:
    '''

    def __init__(self, input_list: List[str]):
        '''
        Initialization method for the class:
        '''

        # Reinitializing these to so the previously passed list is erased,
        # since the __init__ method is being called on the same class-object
        # in the calling function, using a loop.
        self.TAG_LIST :List[str] = []
        self.ID_LIST :List[int] = []
        for item in input_list:
            self.TAG_LIST.append(item.replace("#", ""))

    def __repr__(self):
        '''
        Representation method for the class:
        '''
        return f"{self.TAG_LIST}"

    def resolve_tags(self):
        '''
        Method to check if the passed tags exist in the database table:
        If they exist, return their IDs.
        If they do not exist, add them to the library and return their IDs.
        '''
        for item in self.TAG_LIST:
            tag = Tag.objects.filter(name=item).first()
            if not tag:
                new_tag = Tag(name=item)
                new_tag.save()
                self.ID_LIST.append(new_tag.id)
            elif tag:
                self.ID_LIST.append(tag.id)
        return self.ID_LIST

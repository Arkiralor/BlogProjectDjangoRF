from .models import Blog, Tag
from typing import List


class TagUtils:
    # TAG_LIST = []
    # ID_LIST = []

    def __init__(self, input_list: List[any]):
        self.TAG_LIST = []
        self.ID_LIST = []
        for item in input_list:
            self.TAG_LIST.append(item.replace("#", ""))

    def __repr__(self):
        return f"{self.TAG_LIST}"

    def resolve_tags(self):
        for item in self.TAG_LIST:
            tag = Tag.objects.filter(name=item).first()
            if not tag:
                new_tag = Tag(name=item)
                new_tag.save()
                self.ID_LIST.append(new_tag.id)
            elif tag:
                self.ID_LIST.append(tag.id)
        print("List of hashtag IDs: ", self.ID_LIST)
        print(self)
        return self.ID_LIST

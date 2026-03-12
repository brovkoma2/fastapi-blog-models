from typing import Dict, Any


class Storage:
    def __init__(self):
        self.categories: Dict[int, dict] = {}
        self.users: Dict[int, dict] = {}
        self.posts: Dict[int, dict] = {}
        self.comments: Dict[int, dict] = {}

        self.counters = {
            "categories": 0,
            "users": 0,
            "posts": 0,
            "comments": 0
        }

    def get_next_id(self, entity_type: str) -> int:
        self.counters[entity_type] += 1
        return self.counters[entity_type]


storage = Storage()
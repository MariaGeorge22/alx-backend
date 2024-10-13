#!/usr/bin/env python3
"""LIFO caching module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            if key not in self.cache_data.keys() and\
                    len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                key_to_discard = self.keys.pop()
                print(f"DISCARD: {key_to_discard}")
                del self.cache_data[key_to_discard]
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """return the value in self.cache_data
        linked to key
        """
        if key:
            try:
                return self.cache_data[key]
            except KeyError:
                pass

        return None

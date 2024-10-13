#!/usr/bin/env python3
"""MRU caching module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.access_time = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            # print(f"self.access_count on put: {self.access_time}")
            if key not in self.cache_data.keys() and\
                    len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                max_access = max(self.access_time.values())
                key_to_discard = list(filter(lambda k: self.access_time[k] ==
                                             max_access,
                                             self.access_time.keys()))[0]
                print(f"DISCARD: {key_to_discard}")
                del self.cache_data[key_to_discard]
                del self.access_time[key_to_discard]
            self.cache_data[key] = item
            self.access(key)

    def get(self, key):
        """return the value in self.cache_data
        linked to key
        """
        if key:
            try:
                result = self.cache_data[key]
                self.access(key)
                # print(f"self.access_count on get: {self.access_time}")
                return result
            except KeyError:
                pass

        return None

    def access(self, key):
        """sets access(get or put) for recently used algorithms"""
        last_access = max(self.access_time.values()) if self.access_time else 0
        self.access_time[key] = last_access + 1

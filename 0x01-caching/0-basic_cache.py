#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching
    and is a caching system
    """

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

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

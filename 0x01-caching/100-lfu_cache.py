#!/usr/bin/env python3
"""LFU caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.access_time = {}
        self.access_count = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            # print(f"self.access_time on put: {self.access_time}")
            # print(f"self.access_count on put: {self.access_count}")
            if key not in self.cache_data.keys() and\
                    len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                # LFU
                min_count = min(self.access_count.values())
                discard_list = list(filter(lambda k: self.access_count[k] ==
                                           min_count,
                                           self.access_count.keys()))
                if len(discard_list) != 1:
                    # LRU
                    lfu_access_time = {k: self.access_time[k]
                                       for k in discard_list
                                       if k in self.access_time}
                    min_access = min(lfu_access_time.values())
                    key_to_discard = list(filter(lambda k: lfu_access_time[k]
                                                 == min_access,
                                                 discard_list))[0]
                else:
                    key_to_discard = discard_list[0]
                print(f"DISCARD: {key_to_discard}")
                del self.cache_data[key_to_discard]
                del self.access_time[key_to_discard]
                del self.access_count[key_to_discard]
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
                # print(f"self.access_time on get: {self.access_time}")
                # print(f"self.access_count on get: {self.access_count}")
                return result
            except KeyError:
                pass

        return None

    def access(self, key):
        """sets access(get or put) for recently used algorithms"""
        self.access_count[key] = self.access_count.get(key, 0) + 1
        last_access = max(self.access_time.values()) if self.access_time else 0
        self.access_time[key] = last_access + 1

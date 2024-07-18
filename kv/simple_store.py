class KeyValueStore:
    def __init__(self):
        """Initialize the dictionary to store the key-value pairs."""
        self.store = {}

    def set(self, key, value):
        """Set the value of the key in the store"""
        self.store[key] = value

    def get(self, key):
        """Get the value of the key from the store"""
        return self.store.get(key)

    def delete(self, key):
        """Delete the value of the key from the store"""
        if key in self.store:
            del self.store[key]
        else:
            raise KeyError

    def has_key(self, key):
        """Check if the key exists in the store"""
        return key in self.store

    def all_keys(self):
        """Get all the keys in the store"""
        return list(self.store.keys())


store = KeyValueStore()
store.set("name", "mary")
store.set("email", "mary@example.com")

print("Name: ", store.get("name"))

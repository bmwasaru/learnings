import json
import os


class SimpleDB:
    def __init__(self, filename):
        """Initialize the database with a file name."""
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load data from a file, return empty dict if file doesn't exist."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return {}

    def commit(self):
        """Write the current in-memory data to the file."""
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create(self, key, value):
        """Create a new entry in the database."""
        if key in self.data:
            raise Exception('Key already exists.')
        self.data[key] = value
        self.commit()

    def read(self, key):
        """Read an entry from the database."""
        return self.data.get(key, None)

    def update(self, key, value):
        """Update an existing entry in the database."""
        if key not in self.data:
            raise Exception('Key does not exist.')
        self.data[key] = value
        self.commit()

    def delete(self, key):
        """Delete an entry from the database."""
        if key in self.data:
            del self.data[key]
            self.commit()
        else:
            raise Exception('Key does not exist.')


# Usage example
db = SimpleDB('my_database.json')
db.create('001', {'name': 'John Doe', 'email': 'john@example.com'})
print(db.read('001'))
db.update('001', {'name': 'John Doe', 'email': 'john.d@example.com'})
print(db.read('001'))
db.delete('001')

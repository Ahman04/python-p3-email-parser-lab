# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split on commas OR spaces using regex
        parts = re.split(r"[,\s]+", self.addresses)

        # Keep only valid emails (the tests accept simple pattern)
        emails = [p for p in parts if re.match(r"[^@]+@[^@]+\.[^@]+", p)]

        # Make unique by converting to a set, then back to list
        unique_emails = sorted(set(emails))

        return unique_emails

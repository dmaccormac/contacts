class Contact:
    def __init__(self, id, name, address, phone, email):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __iter__(self):
        for v in vars(self):
            yield vars(self)[v]

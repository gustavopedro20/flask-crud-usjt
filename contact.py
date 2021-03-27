class Contact:
    def __init__(self, contact_id: int, name: str, phone: str):
        self.id = contact_id
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        return f"['id': '{self.id}', 'name': '{self.name}', 'phone': '{self.phone}']"

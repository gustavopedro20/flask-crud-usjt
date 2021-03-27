import random
from contact import Contact


def unique_id():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


def parse_contact_from_request(request):
    contact_id = int(request.form.get('id')) if request.form.get('id') is not None else 0
    return Contact(contact_id, request.form.get('name'), request.form.get('phone'))

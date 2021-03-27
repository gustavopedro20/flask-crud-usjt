from flask import Flask, render_template, request, redirect
from utils import unique_id, parse_contact_from_request
from contact import Contact
import names

app = Flask(__name__)
sequence_id = unique_id()

SCHEDULE_CACHE = []

for i in range(1, 20):
    SCHEDULE_CACHE.append(Contact(next(sequence_id), names.get_full_name(), '1' + str(next(sequence_id))))


@app.route('/')
def schedule():
    return render_template('schedule.html', schedule=SCHEDULE_CACHE)


@app.route('/delete/<int:contact_id>')
def delete(contact_id):
    contact = next((c for c in SCHEDULE_CACHE if c.id == contact_id), None)
    SCHEDULE_CACHE.remove(contact) if contact is not None else None
    return redirect(location='/')


@app.route('/edit/<int:contact_id>')
def contact_edit_redirect(contact_id):
    contact = next((c for c in SCHEDULE_CACHE if c.id == contact_id), {})
    return render_template('contact-edit.html', contact=contact)


@app.route('/create')
def contact_create_redirect():
    return render_template('contact-create.html', contact={})


@app.route('/create/save', methods=['POST'])
def contact_create():
    contact = parse_contact_from_request(request)
    contact.id = next(sequence_id)
    SCHEDULE_CACHE.append(contact)
    return redirect(location='/')


@app.route('/edit/save', methods=['POST'])
def contact_update():
    contact = parse_contact_from_request(request)
    for index, item in enumerate(SCHEDULE_CACHE):
        if item.id == contact.id:
            SCHEDULE_CACHE[index] = contact
            break
    return redirect(location='/')


@app.route('/view/<int:contact_id>')
def contact_view_redirect(contact_id):
    return render_template('contact-view.html', contact=next((c for c in SCHEDULE_CACHE if c.id == contact_id), {}))


if __name__ == '__main__':
    app.run()

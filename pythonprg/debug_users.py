from attendance_app import create_app
from attendance_app.extensions import db
from attendance_app.models import User

app = create_app()
with app.app_context():
    users = User.query.all()
    if not users:
        print('No users found')
    for u in users:
        print(f'username={u.username!r}, name={u.name!r}, role={u.role!r}, pw_hash={u.password!r}')

    # Ensure admin exists
    if not User.query.filter_by(username='admin').first():
        a = User(username='admin', name='Administrator', role='admin')
        a.set_password('password')
        db.session.add(a)
        db.session.commit()
        print('Created admin: username=admin password=password')
    else:
        print('admin already exists')

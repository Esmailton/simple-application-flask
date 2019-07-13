from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Permission:
    LOW = 1
    MEDIUM = 2
    HIGH = 4
    ADMIN = 8


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('UserModel',
                            backref='Role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():

        roles = {

            'LOW': [Permission.LOW],
            'MEDIUM': [Permission.LOW, Permission.MEDIUM],
            'HIGH': [Permission.LOW, Permission.MEDIUM, Permission.HIGH],
            'ADMIN': [Permission.LOW, Permission.MEDIUM,
                      Permission.MEDIUM, Permission.ADMIN]
        }

        default_role = 'LOW'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(25), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    active = db.Column(db.Boolean)
    avatar = db.Column(db.String(200))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def user_exists(self, username):
        return UserModel.query.filter(UserModel.username == username).first()

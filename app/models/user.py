from datetime import datetime
from app import db, bcrypt

# Alias common DB names
Column = db.Column
Model = db.Model
relationship = db.relationship


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(Model):
    __tablename__ = "roles"
    id = Column(db.Integer, primary_key=True, info='角色ID')
    name = Column(db.String(64), unique=True, info='角色名称')
    default = Column(db.Boolean, default=False, index=True, info='name==User时为True')
    permissions = Column(db.Integer, unique=True, info='角色权限')
    description = Column(db.String(50))
    create_time = Column(db.DateTime, default=datetime.utcnow, info='创建时间')
    update_time = Column(db.DateTime, default=datetime.utcnow, info='更新时间')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def __repr__(self):
        return f"<{self.name} - {self.id}>"

    @staticmethod
    def insert_roles():
        roles = {
            "User": [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            "Moderator": [
                Permission.FOLLOW,
                Permission.COMMENT,
                Permission.WRITE,
                Permission.MODERATE,
            ],
            "Admin": [
                Permission.FOLLOW,
                Permission.COMMENT,
                Permission.WRITE,
                Permission.MODERATE,
                Permission.ADMIN,
            ],
        }

        default_role = "User"
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permission()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permission(self):
        self.permissions = 0


class User(Model):
    """ User model for storing user related data """

    id = Column(db.Integer, primary_key=True, unique=True, info='用户ID')
    email = Column(db.String(64), unique=True, index=True, info='邮箱')
    username = Column(db.String(15), unique=True, index=True, info='用户名')
    name = Column(db.String(64), info='姓名')
    password_hash = Column(db.String(128), info='密码')
    role_id = Column(db.Integer, info='角色ID')
    create_time = db.Column(db.DateTime, default=datetime.utcnow, info='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.utcnow, info='更新时间')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # 生成一个User对象，自动更新create_time和update_time
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    @property
    def password(self):
        raise AttributeError("密码是不可读")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"

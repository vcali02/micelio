# flask extension; import the class
from config import db, bcrypt
from flask_sqlalchemy import SQLAlchemy
# the metadata class is used to store/represent database metadata
# usually: python classes called ORM models
# metadata class: define additional database structure
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

# import library
# adds .to_dict() method to model instances
# allows control over max recursion
from sqlalchemy_serializer import SerializerMixin
# an instance of MetaData
metadata = MetaData(naming_convention={
    # specifies how the name of the foreign key should be generated
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
# an instance of SQLAlchemy
# db = SQLAlchemy()

# password hashing

# associating MetaData instance with the SQLAlchemy instance to define/manage
# the structure of the database tables

################ USER################


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    image = db.Column(db.String)
    bio = db.Column(db.String)

    # RELATIONSHIP
    # -one user has many completed prompts; many prompts are completed by one user
    completed_prompts = db.relationship(
        "CompletedPrompt", back_populates="user")

    # ASSOCIATION PROXY
    # -one user has completed nudges through completed prompts
    completed_nudges = association_proxy("completed_prompts", "nudge_prompt")
    # -one user has completed journals through completed prompts
    completed_journals = association_proxy(
        "completed_prompts", "journal_prompt")

    # SERIALIZE RULES
    serialize_rules = (
        # "-completed_nudges.nudge_prompt",
        # "-completed_journals.journal_prompt",
        # "-completed_prompts.user"
        "-_password_hash",
    )

    # AUTH VALIDATION
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    # VALIDATION

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Must include a name.")
        if len(name) < 1:
            raise ValueError("Name must be at least 1 character.")
        return name

    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Must include a username.")
        if len(username) < 5:
            raise ValueError("Username must be at least 5 characters.")
        return username

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError('Must be a valid email address.')
        return address

    # VALIDATE PASSWORD#


################ COMPLETED PROMPTS################
class CompletedPrompt(db.Model, SerializerMixin):
    __tablename__ = "completed_prompts"

    id = db.Column(db.Integer, primary_key=True)

    # FOREIGN KEY
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    nudge_prompt_id = db.Column(db.Integer, db.ForeignKey("nudge_prompts.id"))
    journal_prompt_id = db.Column(
        db.Integer, db.ForeignKey("journal_prompts.id"))

    # RELATIONSHIP
    # -one user has many completed prompts; many prompts are completed by one user
    user = db.relationship("User", back_populates="completed_prompts")
    # -one nudge prompt has many completed prompts; many completed prompts are a nudge prompt
    nudge_prompt = db.relationship(
        "NudgePrompt", back_populates="completed_prompt")
    # -one journal prompt has many completed prompts; many completed prompts are a journal prompt
    journal_prompt = db.relationship(
        "JournalPrompt", back_populates="completed_prompt")

    # SERIALIZE RULES
    serialize_rules = (
        "-nudge_prompt.completed_prompt",
        "-journal_prompt.completed_prompt",
        "-user.completed_prompts"
    )

    # VALIDATION


################ NUDGE PROMPTS################
class NudgePrompt(db.Model, SerializerMixin):
    __tablename__ = "nudge_prompts"

    id = db.Column(db.Integer, primary_key=True)
    action_prompt = db.Column(db.String)
    completed_at = db.Column(db.DateTime, server_default=db.func.now())

    # FOREIGN KEY
    nudges_id = db.Column(db.Integer, db.ForeignKey("nudges.id"))

    # RELATIONSHIP
    # -one nudge prompt has many completed prompts; many completed prompts are a nudge prompt
    completed_prompt = db.relationship(
        "CompletedPrompt", back_populates="nudge_prompt")
    # -one nudge has many prompts; many nudge prompts belong to one nudge
    action_type = db.relationship("Nudge", back_populates="nudge_prompts")

    # SERIALIZE RULES
    serialize_rules = (
        "-completed_prompt.nudge_prompt",
        "-action_type.nudge_prompts",
        "-action_type.pillar"
    )

    # VALIDATION


################ NUDGES################
class Nudge(db.Model, SerializerMixin):
    __tablename__ = "nudges"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    action_type = db.Column(db.String)
    description = db.Column(db.String)

    # FOREIGN KEY
    pillar_id = db.Column(db.Integer, db.ForeignKey("pillars.id"))

    # RELATIONSHIP
    # -one nudge has many prompts; many nudge prompts belong to one nudge
    nudge_prompts = db.relationship(
        "NudgePrompt", back_populates="action_type")
    # -one pillar has one nudge; one nudge has one pillar
    pillar = db.relationship("Pillar", back_populates="nudge")

    # SERIALIZE RULES
    serialize_rules = (
        "-nudge_prompts.action_type",
        "-pillar.nudge",
        "-nudge_prompts.completed_prompt"
    )

    # VALIDATION


################ JOURNAL PROMPTS################
class JournalPrompt(db.Model, SerializerMixin):
    __tablename__ = "journal_prompts"

    id = db.Column(db.Integer, primary_key=True)
    action_prompt = db.Column(db.String)
    completed_at = db.Column(db.DateTime, server_default=db.func.now())

    # FOREIGN KEY
    journals_id = db.Column(db.Integer, db.ForeignKey("journals.id"))

    # RELATIONSHIP
    # -one nudge prompt has many completed prompts; many completed prompts are a nudge prompt
    completed_prompt = db.relationship(
        "CompletedPrompt", back_populates="journal_prompt")
    # -one journal has many prompts; many journal prompts belong to one journal
    action_type = db.relationship("Journal", back_populates="journal_prompts")

    # SERIALIZE RULES
    serialize_rules = (
        "-completed_prompt.journal_prompt",
        "-action_type.journal_prompts",
        "-action_type.pillar"
    )

    # VALIDATION


################ JOURNALS################
class Journal(db.Model, SerializerMixin):
    __tablename__ = "journals"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    action_type = db.Column(db.String)
    description = db.Column(db.String)

    # FOREIGN KEY
    pillar_id = db.Column(db.Integer, db.ForeignKey("pillars.id"))

    # RELATIONSHIP
    # -one journal has many prompts; many journal prompts belong to one journal
    journal_prompts = db.relationship(
        "JournalPrompt", back_populates="action_type")
    # -one pillar has one journal; one journal has one pillar
    pillar = db.relationship("Pillar", back_populates="journal")

    # SERIALIZE RULES
    serialize_rules = (
        "-journal_prompts.action_type",
        "-pillar.journal",
        "-journal_prompts.completed_prompt"
    )

    # VALIDATION


################ PILLARS################
class Pillar(db.Model, SerializerMixin):
    __tablename__ = "pillars"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    pillar_name = db.Column(db.String)
    description = db.Column(db.String)

    # FOREIGN KEY
    # none at this time

    # RELATIONSHIP
    # -one pillar has one nudge; one nudge has one pillar
    nudge = db.relationship("Nudge", back_populates="pillar")
    # -one pillar has one journal; one journal has one pillar
    journal = db.relationship("Journal", back_populates="pillar")

    # SERIALIZE RULES
    serialize_rules = (
        "-nudge.pillar",
        "-journal.pillar",
    )


################ RECOMMENDATIONS################
class Recommendation(db.Model, SerializerMixin):
    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)
    rec_type = db.Column(db.String)
    rec_link = db.Column(db.String)
    image = db.Column(db.String)
    blurb = db.Column(db.String)

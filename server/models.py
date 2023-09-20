from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if name == "":
            raise ValueError("Each record requires a name")
        return name

    @validates("phone_number")
    def validate_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("A phone number must be 10 digits.")
        return phone_number

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("title")
    def validate_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(word in title for word in clickbait):
            raise ValueError("A title requires clickbait words.")
        return title

    @validates("content")
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("A post must be at least 250 characters.")
        return content

    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("A summary cannot be more than 250 characters.")
        return summary

    @validates("category")
    def validate_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError("A post's category must be Fiction or Non-Fiction")
        return category

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"

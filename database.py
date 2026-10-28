import psycopg
from psycopg.rows import dict_row
import os
from dotenv import load_dotenv
load_dotenv()
class Database:
    def __init__(self):
        self.connection=psycopg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password=os.getenv("password"),
            dbname="notesystem",
            row_factory=dict_row
        )
        self.cursor=self.connection.cursor()

    def add_note(self,note):
        try:
            self.cursor.execute(
                "insert into notes(title,description)" \
                " values(%s,%s)",(note.title,note.description)
            )
            self.connection.commit()
            return True

        except psycopg.errors.NotNullViolation as e:
            self.connection.rollback()
            return "NotNullViolation Error."
        except psycopg.errors.UniqueViolation as e:
            self.connection.rollback()
            return "UniqueViolation Error"
        except psycopg.Error as e:
            self.connection.rollback()
            return False

    def get_notes(self):
        try:
            self.cursor.execute(
                "select * from notes"
            )
            rows=self.cursor.fetchall()
            return rows
        except psycopg.Error as e:
            print(e)
            return None

    def update_notes(self,note_id,note):
        try:
            self.cursor.execute(
                "update notes" \
                " set title=%s, description=%s, updated_at=current_timestamp" \
                " where note_id =%s returning *",(note.title,note.description,note_id)
            )
            row=self.cursor.fetchone()
            if row is None:
                return None
            self.cursor.execute(
                "insert into updated_note(note_id,title,description,created_at,updated_at)" \
                " values(%s,%s,%s,%s,%s)",(row["note_id"],row["title"],row["description"],row["created_at"],row["updated_at"])
            )
            self.connection.commit()
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            print(e)
            return False

    def delete_note(self,note_id):
        try:
            self.cursor.execute(
                "delete from notes" \
                " where note_id=%s returning *",(note_id,)
            )
            row=self.cursor.fetchone()
            if row is None:
                return None
            self.cursor.execute(
                "insert into deleted_note(note_id,title,description,created_at)" \
                " values(%s,%s,%s,%s)",(row["note_id"],row["title"],row["description"],row["created_at"])
            )
            self.connection.commit()
            return True
        except psycopg.Error as e:
            self.connection.rollback()
            return False

    def search_note_id(self,note_id):
        try:
            self.cursor.execute(
                "select * from notes" \
                " where note_id=%s",(note_id,)
            )
            row=self.cursor.fetchone()
            return row
        except psycopg.Error as e:
            print(e)
            return False
    def search_note_title(self,title):
        try:
            self.cursor.execute(
                "select * from notes" \
                " where title=%s",(title,)
            )
            row=self.cursor.fetchone()
            return row
        except psycopg.Error as e:
            print(e)
            return False

    def view_updated_history(self):
        try:
            self.cursor.execute(
                "select * from updated_note" \
                " order by note_id,history_id"
            )
            rows=self.cursor.fetchall()
            return rows
        except psycopg.Error as e:
            print(e)
            return False

    def view_deleted_history(self):
        try:
            self.cursor.execute(
                "select * from deleted_note" \
                " order by note_id"
            )
            rows=self.cursor.fetchall()
            return rows
        except psycopg.Error as e:
            print(e)
            return False
        

        
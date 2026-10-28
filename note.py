class Note:
    def __init__(self,title,description,note_id=None,created_at=None,updated_at=None,deleted_at=None):
        self.title=title
        self.description=description
        self.note_id=note_id
        self.created_at=created_at
        self.updated_at=updated_at
        self.deleted_at=deleted_at
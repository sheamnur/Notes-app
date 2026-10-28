from database import Database
from note import Note
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
database=Database()
app=FastAPI()
class Notes(BaseModel):
    title:str
    description:str

class NoteUpdate(BaseModel):
    title:str| None=None
    description:str| None=None

@app.post("/notes",status_code=201)
def add_notes(note:Notes):
    title=note.title
    description=note.description
    note=Note(title,description)
    result=database.add_note(note)
    if isinstance(result,str):
        raise HTTPException(status_code=422,detail=result)
    elif result is True:
        return{"Message":"Notes added successfully."}
    else:
        raise HTTPException(status_code=500,detail="Internal server error.")

@app.get("/notes")
def ViewAllNote():
    notes=database.get_notes()
    if notes is None:
        raise HTTPException(status_code=500,detail="Internal server error.")
    return notes

@app.get("/notes/id/{note_id}")
def SearchById(note_id:int):
    result=database.search_note_id(note_id)
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    if result is None:
        raise HTTPException(status_code=404,detail="Note not found.")
    return{
        "message":"Note found successfully",
        "detail":result
           }

@app.get("/notes/title/{title}")
def SearchByTitle(title:str):
    result=database.search_note_title(title)
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    if result is None:
        raise HTTPException(status_code=404,detail="Note not found.")
    return{
        "message":"Note found successfully",
        "detail":result
           }

@app.patch("/notes/{note_id}")
def update_note(note_id:int,note:NoteUpdate):
    data=database.search_note_id(note_id)
    if data is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    if data is None:
        raise HTTPException(status_code=404,detail="Note not found.")

    update_data=note.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400,detail="At least one field must be provided")
    for key in Notes.model_fields:
        if key not in update_data:
            update_data[key]=data[key]
    note=Note(update_data["title"],update_data["description"])
    result=database.update_notes(note_id,note)
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    if result is None:
        raise HTTPException(status_code=404,detail="Note not found.")
    return{"message":"Note updated successfully."}

@app.delete("/notes/{note_id}")
def delete_note(note_id:int):
    result=database.delete_note(note_id)
    if result is None:
        raise HTTPException(status_code=404,detail="Note is not exist.")
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    return{"message":"Note successfully deleted."}

@app.get("/notes/deleted")
def view_deleted_note():
    result=database.view_deleted_history()
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    return result

@app.get("/notes/updated")
def view_updated_note():
    result=database.view_updated_history()
    if result is False:
        raise HTTPException(status_code=500,detail="Internal server error.")
    return result

    
import ast
notes=[]

with open("note.txt","a") as file:
        pass
with open("note.txt","r") as file:
    for line in file:
        notes.append(ast.literal_eval(line.strip()))

def add_notes():
    note_id=input("Enter id of this note: ")
    note_name=input("Enter the name of the note: ")
    note_content=input("Enter content: ")
    notes.append([note_id,note_name,note_content])
    with open("note.txt","a") as file:
        file.write(str(([note_id,note_name,note_content]))+"\n")
    

def view_notes():
    if len(notes)==0:
        print("Notepad is empty")
        return
    for i in notes:
        print(i)


def search_notes():
    if len(notes)==0:
        print("Notepad is empty")
        return
    id=input("Enter note id: ")
    for i in notes:
        if i[0]==id:
            print(i)
    


def edit_notes():
    if len(notes)==0:
        print("Notepad is empty")
        return
    id=input("NOte id for edit: ")
    for i in notes:
        if i[0]==id:
            print("Note is found.")
            a=input("1 for edit name, 2 for edit edit content")
            if a=="1":
                i[1]=input("Enter new name: ")
            elif a=="2":
                i[2]=input("Enter new content: ")
            print(i)
    with open("note.txt","w") as file:
        for line in notes:
            file.write(str(line)+"\n")
               

def delete_notes():
    if len(notes)==0:
        print("Notepad is empty")
        return
    id=input("Enter note id you want to delete: ")
    for i in notes:
        if i[0]==id:
            notes.remove(i)
            print("Remove successfull.")
    with open("note.txt","w") as file:
        for line in notes:
            file.write(str(line)+"\n")
               
               

 
while True:
    print("Enter 1 to add note")
    print("Enter 2 to view all notes")
    print("Enter 3 to search notes")
    print("Enter 4 to edit note")
    print("Enter 5 to delete note")
    print("Enter 6 to exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_notes()
    elif choice==2:
        view_notes()
    elif choice==3:
        search_notes()
    elif choice==4:
        edit_notes()
    elif choice==5:
        delete_notes()
        
    elif choice==6:
        break
    else:
        print("Invalid choice.")
    
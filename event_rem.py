import tkinter
import tkinter.messagebox
import event_dbc

window = tkinter.Tk()
window.title("Reminder")
#window.geometry("800x500")

#functions

def add_event():
    task = entry_event.get().split('-')
    print(task[0])
    print(task[1])
    if task!="":
        listbox_event.insert(tkinter.END, task)
        entry_event.delete(0, tkinter.END)
        event_dbc.disp()
    else:
        tkinter.messagebox.showwarning(title="Warning", message="enter an event")

def update_event():
    pass

def delete_event():
    pass

#createGUI

frame_event = tkinter.Frame(window)
frame_event.pack()

listbox_event = tkinter.Listbox(frame_event, height=15, width=50)
listbox_event.pack(side=tkinter.LEFT)

scrollbar_event = tkinter.Scrollbar(frame_event)
scrollbar_event.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_event.config(yscrollcommand=scrollbar_event.set)
scrollbar_event.config(command=listbox_event.yview)

entry_event=tkinter.Entry(window, width=50)
entry_event.pack()

button_add_event = tkinter.Button(window, text="add event",width=48,command=add_event)
button_add_event.pack()

button_update_event = tkinter.Button(window, text="update event",width=48,command=update_event)
button_update_event.pack()

button_delete_event = tkinter.Button(window, text="delete event",width=48,command=add_event)
button_delete_event.pack()

window.mainloop()

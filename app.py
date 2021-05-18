import tkinter as tk
import tkinter.scrolledtext as st
import main

fields = 'Age', 'Pin-code' , 'Number of Days'
display=[]

def fetch(entries):
    global display

    info=list()
    for entry in entries:
        info.append(entry[1].get())
    age=int(info[0])
    pincodes=list()
    pincodes.append(info[1])
    num_days=int(info[2])
    display=main.search(age,pincodes,num_days)
    for detail in display:
        s=f"Pincode: {detail['pincode']} \n Available on: {detail['given_date']} \n {detail['center_name']} \n {detail['block_name']} \n Price:  {detail['fee_type']} \n Availablity :  {detail['Availablity']}\ns"
        if detail['Vaccine']!='':
            s+=f"\n Vaccine Type: {detail['Vaccine']}"
        text_area.insert(tk.INSERT,s)
    text_area.config(state='disabled')

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    button_frame = tk.Frame(root)
    b1 = tk.Button(button_frame, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b2 = tk.Button(button_frame, text='Quit', command=root.quit)
    button_frame.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    text_frame = tk.Frame(root)
    text_area = st.ScrolledText(text_frame,wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))
    text_frame.pack(side=tk.BOTTOM,fill=tk.X, padx=5, pady=5)
    text_area.pack(padx=5, pady=5)
    root.mainloop()
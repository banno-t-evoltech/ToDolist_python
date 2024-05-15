# encoding: utf-8
import os
import tkinter as tk
import tkinter.messagebox as mb

app = tk.Tk()
app.geometry('350x350')
app.title('ToDoList')

lb1_1 = tk.Label(text='日付と予定を入力して予定を追加ボタンを押してください')
lb1_1.place(x=30,y=30)

lbl = tk.Label(text='日付')
lbl.place(x=30, y=50)

lb2 = tk.Label(text='予定')
lb2.place(x=30, y=70)

txt1 = tk.Entry(width=20)
txt1.place(x=90, y=50)

txt2 = tk.Entry(width=20)
txt2.place(x=90, y=70)

txt3 = tk.Entry(width=4)
txt3.place(x=150, y=260)

lb3 = tk.Label(text='ポップアップで< [番号]予定> を順番に出力します')
lb3.place(x=50, y=170)

lb4 = tk.Label(text='上記テキストボックスに入力した予定を追加します')
lb4.place(x=50, y=230)

lb5 = tk.Label(text='[番号]:')
lb5.place(x=110, y=260)
lb5 = tk.Label(text='"予定を出力"ボタンで出力した[番号]を削除します')
lb5.place(x=50, y=290)

#ファイル
todofile = 'todo.txt'

#呼び出し
def load_todo():
    global todo1
    if os.path.exists(todofile):
        with open(todofile, 'r') as file:
            todo1 = file.readlines()
        todo1 = [todo.strip() for todo in todo1]
    else:
        todo1 = []
    return todo1

#書き込み
def save_todo(todo1):
    with open(todofile, 'w') as file:
        for todo in todo1:
            file.write(todo + '\n')

#予定を追加
def add_todo(todo1, text):
    todo1.append(text)
    save_todo(todo1)

#予定を削除
def delete_todo(todo1, index):
    if 0 <= index < len(todo1):
        todo1.pop(index)
        save_todo(todo1)

def main():
    todos = load_todo()

if __name__ == '__main__':
    main()


#予定を表示
def btn_click1():
    for i, todo in enumerate(todo1):
        print(f"{i}: {todo}")
        mb.showinfo(f'予定を出力', f"[{i}]{todo}") 
btn1 = tk.Button(app, text='予定を出力', command=btn_click1)
btn1.place(x=30, y=140)

#予定を追加
def btn_click2():
    global todo_time
    global todo_schedule
    todo_time, todo_schedule = txt1.get(), txt2.get()
    lb1_2 = tk.Label(text=f'時間: {todo_time}')
    lb1_2.place(x=60, y=100)
    lb2_2 = tk.Label(text=f'予定: {todo_schedule}')
    lb2_2.place(x=130, y=100)
    text = f'{todo_time}' + ': ' +  f'{todo_schedule}'
    add_todo(todo1, text)

btn2 = tk.Button(app, text='予定を追加', command=btn_click2)
btn2.place(x=30, y=200)

#予定を削除
def btn_click3():
    global todo_delete
    todo_delete = txt3.get()
    #index = int(input("削除するToDoの番号を入力してください: "))
    delete_todo(todo1, int(todo_delete))
    for i, todo in enumerate(todo1):
        print(f"{i}: {todo}")
        mb.showinfo(f'予定を出力', f"[{i}]{todo}")
btn3 = tk.Button(app, text='予定を削除', command=btn_click3)
btn3.place(x=30, y=260)

app.mainloop()
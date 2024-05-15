# encoding: utf-8
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry('300x400')
app.title('ToDoList')

lb1_1 = tk.Label(text='日付と予定を入力してください')
lb1_1.place(x=30,y=30)

lbl = tk.Label(text='日付')
lbl.place(x=30, y=50)

lb2 = tk.Label(text='予定')
lb2.place(x=30, y=70)

txt1 = tk.Entry(width=20)
txt1.place(x=90, y=50)

txt2 = tk.Entry(width=20)
txt2.place(x=90, y=70)

#ファイル
todofile = 'todo.txt'

#呼び出し
def load_todo():
    if os.path.exists(todofile):
        with open(todofile, 'r') as file:
            todo = file.readlines()
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
def add_todo(todo1, item):
    todo1.append(item)
    save_todo(todo1)

#予定を削除
def delete_todo(todo1, index):
    if 0 <= index < len(todo1):
        todo1.pop(index)
        save_todo(todo1)

'''
def main():
    todo1 = load_todo()

if __name__ == '__main__':
    main()

    while True:
        command = input("コマンドを入力してください（追加、表示、削除、終了）: ")
        if command == '終了':
            break
        elif command == '追加':
            item = input("ToDo項目を入力してください: ")
            add_todo(todo1, item)
        elif command == '表示':
            for i, todo in enumerate(todo1):
                print(f"{i}: {todo}")
        elif command == '削除':
            index = int(input("削除するToDoの番号を入力してください: "))
            delete_todo(todo1, index)
        else:
            print("無効なコマンドです。")   
'''

#予定を入力
#btn1 = tk.Button(app, text='予定を入力', command=save_todo)
#btn1.place(x=30, y=120)

#予定を表示
btn2 = tk.Button(app, text='予定を出力', command=load_todo)
btn2.place(x=30, y=180)

#予定を追加
def btn_click1():
    global todo_time
    global todo_schedule
    global todo2
    todo_time, todo_schedule = txt1.get(), txt2.get()
    lb1_2 = tk.Label(text=f'時間: {todo_time}')
    lb1_2.place(x=60, y=100)
    lb2_2 = tk.Label(text=f'予定: {todo_schedule}')
    lb2_2.place(x=130, y=100)
    text = f'{todo_time}' + ': ' +  f'{todo_schedule}'
    file = open(todofile, 'w')
    file.write(text)
    file.close()


btn3 = tk.Button(app, text='予定を追加', command=btn_click1)
btn3.place(x=30, y=240)

#予定を削除
btn4 = tk.Button(app, text='予定を削除', command=delete_todo)
btn4.place(x=30, y=300)

app.mainloop()


'''
現在の状況メモ
GUIへの以降が難しい・・・。
予定を１行テキストに追加することはできたが
次に追加しようとすると上書きになって消えてしまう。

予定の表示、削除についてはまだボタンだけ作成
'''
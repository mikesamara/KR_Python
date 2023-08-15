#Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента

import json
import os
import datetime
 
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    def to_dict(self):
        return {"title": self.title, "content": self.content, "timestamp": self.timestamp}
 
def load_notes():
    notes = []
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes_data = json.load(file)
            for note_data in notes_data:
                note = Note(note_data["title"], note_data["content"])
                note.timestamp = note_data["timestamp"]
                notes.append(note)
    return notes
 
def save_notes(notes):
    notes_data = [note.to_dict() for note in notes]
    with open("notes.json", "w") as file:
        json.dump(notes_data, file, indent=4)
 
def view_notes(notes):
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note.title} - {note.content} - {note.timestamp}")
 
def add_note(notes):
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    new_note = Note(title, content)
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена.")
 
def edit_note(notes):
    view_notes(notes)
    idx = int(input("Введите номер заметки для редактирования: ")) - 1
    if 0 <= idx < len(notes):
        note = notes[idx]
 
        new_title = input("Введите новый заголовок заметки: ")
        new_content = input("Введите новый текст заметки: ")
 
        edited_note = Note(new_title, new_content)
        
        notes[idx] = edited_note
 
        save_notes(notes)
        print("Заметка успешно отредактирована.")
    else:
        print("Неверный номер заметки.")
 
def delete_note(notes):
    view_notes(notes)
    idx = int(input("Введите номер заметки для удаления: ")) - 1
    if 0 <= idx < len(notes):
        del notes[idx]
        save_notes(notes)
        print("Заметка успешно удалена.")
    else:
        print("Неверный номер заметки.")
 
def main():
    notes = load_notes()
 
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
 
        choice = input()
        if choice == "1":
            view_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")
 
if __name__ == "__main__":
    main()
from view import *
from presenter import *
from model import *
from note import *


note_1 = Note("1", "Python", "Популярный язык программирования")
note_2 = Note("2", "Java", "Строго типизированный язык програмирования")
note_3 = Note("3", "SQL", "Декларативный язык программирования")
note_4 = Note("4", "HTML", "Язык гипертекстовой разметки")
notes: Note = [note_1, note_2, note_3, note_4]


model_obj = Model(notes)
view_obj = View()
presenter_obj = Presenter(model_obj, view_obj)
presenter_obj.start()
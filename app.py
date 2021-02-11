import tkinter as tk
from typing import Text
import mysql.connector

from tkinter.ttk import *
from tkinter import messagebox

def criar_tabela():
    dgv_testes['columns'] = ('ID', 'Título', 'Data', 'Base de Dados', 'Técnica', 'Acurácia', 'Precisão', 'Deficiência', 'Desafio')

    dgv_testes.column('#0', width=0, minwidth=0, anchor='n')
    dgv_testes.column('ID', width=25, minwidth=25, anchor='n')
    dgv_testes.column('Título', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Data', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Base de Dados', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Técnica', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Acurácia', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Precisão', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Deficiência', width=100, minwidth=25, anchor='n')
    dgv_testes.column('Desafio', width=100, minwidth=25, anchor='n')

    dgv_testes.heading('#0', text='', anchor='n')
    dgv_testes.heading('ID', text='ID', anchor='n')
    dgv_testes.heading('Título', text='Título', anchor='n')
    dgv_testes.heading('Data', text='Data', anchor='n')
    dgv_testes.heading('Base de Dados', text='Base de Dados', anchor='n')
    dgv_testes.heading('Técnica', text='Técnica', anchor='n')
    dgv_testes.heading('Acurácia', text='Acurácia', anchor='n')
    dgv_testes.heading('Precisão', text='Precisão', anchor='n')
    dgv_testes.heading('Deficiência', text='Deficiência', anchor='n')
    dgv_testes.heading('Desafio', text='Desafio', anchor='n')

def carregar_tabela():
    try:
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Tamanda010203',
            database = 'covid'
        )
        
        cursor = db.cursor()
        cursor.execute('SELECT * FROM covid.testes;')
        resultados = cursor.fetchall()
        db.commit()

        for row in resultados:
            dgv_testes.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))


    except Exception as ex:
            messagebox.showwarning('Erro', ex)

    finally:
        db.close();

window = tk.Tk()
window.title('TESTES COVID IA')

dgv_testes = Treeview(window)
criar_tabela()
dgv_testes.grid(column=0, row=0, padx=3, pady=3, sticky='N')
carregar_tabela()

window.mainloop()
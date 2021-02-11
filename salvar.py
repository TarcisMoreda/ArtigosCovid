import tkinter as tk
import mysql.connector

from tkinter.constants import DISABLED, LEFT
from tkinter import messagebox
from tkcalendar import *

def salvar():
    titulo = txt_titulo.get()
    data = dtp_data.get_date()
    base_dados = txt_base_dados.get()
    tecnica = txt_tecnica.get()
    acuracia = txt_acuracia.get()
    precisao = txt_precisao.get()
    deficiencia = txt_deficiencia.get()
    desafio = txt_desafio.get()

    if titulo == '' or tecnica == '' or acuracia == '' or precisao == '' or desafio == '' or base_dados == '' or  deficiencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos.')

    else:
        try:
            db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Tamanda010203',
            database = 'covid'
            )
        
            cursor = db.cursor()
            cursor.execute('INSERT INTO `covid`.`testes` (`titulo`, `data`, `base_dados`, `tecnica`, `acuracia`, `precisao`, `deficiencia`, `desafio`) VALUES ("%s", STR_TO_DATE("%s","%%d/%%m/%%Y"), "%s", "%s", "%s", "%s", "%s", "%s");' %(titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio))
            db.commit()

            messagebox.showinfo('Sucesso', 'Adicionado com sucesso ao banco de dados.')

        except Exception as ex:
            messagebox.showwarning('Erro', ex)

        finally:
            db.close()

window = tk.Tk()
window.title('COVID-19 TESTES')

lbl_id = tk.Label(window, text='ID:')
lbl_id.grid(column=0, row=0, padx=3, pady=3, sticky='W')

txt_id = tk.Entry(window, width=5, state=DISABLED)
txt_id.grid(column=0, row=1, padx=3, pady=3, sticky='NW')

lbl_titulo = tk.Label(window, text='Título:')
lbl_titulo.grid(column=1, row=0, padx=3, pady=3, sticky='W')

txt_titulo = tk.Entry(window, width=25, justify=LEFT)
txt_titulo.grid(column=1, row=1, padx=3, pady=3, sticky='NW')

lbl_data = tk.Label(window, text='Data:')
lbl_data.grid(column=2, row=0, padx=3, pady=3, sticky='W')

dtp_data = Calendar(window, selectmode='day')
dtp_data.grid(column=2, row=1, padx=3, pady=3, sticky='NW')

lbl_base_dados = tk.Label(window, text='Base de Dados:')
lbl_base_dados.grid(column=0, row=2, padx=3, pady=3, sticky='W')

txt_base_dados = tk.Entry(window, width=25, justify=LEFT)
txt_base_dados.grid(column=0, row=3, padx=3, pady=3, sticky='NW')

lbl_tecnica = tk.Label(window, text='Técnica Utilizada:')
lbl_tecnica.grid(column=1, row=2, padx=3, pady=3, sticky='W')

txt_tecnica = tk.Entry(window, width=25, justify=LEFT)
txt_tecnica.grid(column=1, row=3, padx=3, pady=3, sticky='NW')

lbl_acuracia = tk.Label(window, text='Acurácia:')
lbl_acuracia.grid(column=2, row=2, padx=3, pady=3, sticky='W')

txt_acuracia = tk.Entry(window, width=25, justify=LEFT)
txt_acuracia.grid(column=2, row=3, padx=3, pady=3, sticky='NW')

lbl_precisao = tk.Label(window, text='Previsão:')
lbl_precisao.grid(column=0, row=4, padx=3, pady=3, sticky='W')

txt_precisao = tk.Entry(window, width=25, justify=LEFT)
txt_precisao.grid(column=0, row=5, padx=3, pady=3, sticky='NW')

lbl_deficiencia = tk.Label(window, text='Deficiência:')
lbl_deficiencia.grid(column=1, row=4, padx=3, pady=3, sticky='W')

txt_deficiencia = tk.Entry(window, width=25, justify=LEFT)
txt_deficiencia.grid(column=1, row=5, padx=3, pady=3, sticky='NW')

lbl_desafio = tk.Label(window, text='Desafio:')
lbl_desafio.grid(column=2, row=4, padx=3, pady=3, sticky='W')

txt_desafio = tk.Entry(window, width=25, justify=LEFT)
txt_desafio.grid(column=2, row=5, padx=3, pady=3, sticky='NW')

btn_salvar = tk.Button(window, text='Salvar', width=10, height=1, command=salvar)
btn_salvar.grid(column=2, row=6, padx=3, pady=3, sticky='SE')

window.mainloop()
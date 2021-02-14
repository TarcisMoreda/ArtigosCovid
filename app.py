import tkinter as tk
import mysql.connector
import datetime

from tkinter.ttk import *
from tkinter.constants import DISABLED, LEFT, NORMAL
from tkinter import messagebox
from tkcalendar import *

aberto = False

def criar_tabela():
    dgv_artigos['columns'] = ('ID', 'Título', 'Data', 'Base de Dados', 'Técnica', 'Acurácia', 'Precisão', 'Deficiência', 'Desafio')

    dgv_artigos.column('#0', width=0, minwidth=0, anchor='n')
    dgv_artigos.column('ID', width=25, minwidth=25, anchor='n')
    dgv_artigos.column('Título', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Data', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Base de Dados', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Técnica', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Acurácia', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Precisão', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Deficiência', width=100, minwidth=25, anchor='n')
    dgv_artigos.column('Desafio', width=100, minwidth=25, anchor='n')

    dgv_artigos.heading('#0', text='', anchor='n')
    dgv_artigos.heading('ID', text='ID', anchor='n')
    dgv_artigos.heading('Título', text='Título', anchor='n')
    dgv_artigos.heading('Data', text='Data', anchor='n')
    dgv_artigos.heading('Base de Dados', text='Base de Dados', anchor='n')
    dgv_artigos.heading('Técnica', text='Técnica', anchor='n')
    dgv_artigos.heading('Acurácia', text='Acurácia', anchor='n')
    dgv_artigos.heading('Precisão', text='Precisão', anchor='n')
    dgv_artigos.heading('Deficiência', text='Deficiência', anchor='n')
    dgv_artigos.heading('Desafio', text='Desafio', anchor='n')

def carregar_tabela():
    dgv_artigos.delete(*dgv_artigos.get_children())

    try:
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Tamanda010203',
            database = 'testes'
        )
        
        cursor = db.cursor()
        cursor.execute('SELECT * FROM testes.artigos;')
        resultados = cursor.fetchall()
        db.commit()

        for row in resultados:
            dgv_artigos.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    except Exception as ex:
            messagebox.showwarning('Erro', ex)

    finally:
        db.close()

def selecionar_id():
    try:
        item_atual = dgv_artigos.focus()
        return (dgv_artigos.item(item_atual).get('values')[0])

    except:
        messagebox.showwarning('Erro', 'Selecione um item da lista.')

def selecionar_ultimo_id():
    try:
        if len(dgv_artigos.get_children()) != 0:
            ultimo = dgv_artigos.get_children()[-1]
            return (dgv_artigos.item(ultimo).get('values')[0])

    except Exception as ex:
        messagebox.showwarning('Erro', ex)

def escrever_textbox(titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio):
    try:
        item_atual = dgv_artigos.focus()
        tudo = dgv_artigos.item(item_atual).get('values')
        data_formatada = datetime.datetime.strptime(str(tudo[2]), '%Y-%m-%d').strftime('%d/%m/%Y')

        titulo.insert(0, tudo[1])
        data.set_date(data_formatada)
        base_dados.insert(0, tudo[3])
        tecnica.insert(0, tudo[4])
        acuracia.insert(0, tudo[5])
        precisao.insert(0, tudo[6])
        deficiencia.insert(0, tudo[7])
        desafio.insert(0, tudo[8])
    
    except Exception as ex:
            messagebox.showwarning('Erro', ex)

    

def salvar(titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio, txt_id):
    if titulo == '' or tecnica == '' or acuracia == '' or precisao == '' or desafio == '' or base_dados == '' or  deficiencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos.')

    else:
        try:
            db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Tamanda010203',
            database = 'testes'
            )
        
            cursor = db.cursor()
            cursor.execute('INSERT INTO `testes`.`artigos` (`titulo`, `data`, `base_dados`, `tecnica`, `acuracia`, `precisao`, `deficiencia`, `desafio`) VALUES ("%s", STR_TO_DATE("%s","%%Y-%%m-%%d"), "%s", "%s", "%s", "%s", "%s", "%s");' %(titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio))
            db.commit()

            messagebox.showinfo('Sucesso', 'Registrado com sucesso ao banco de dados.')

        except Exception as ex:
            messagebox.showwarning('Erro', ex)

        finally:
            db.close()
            carregar_tabela()
            
            txt_id.config(state=NORMAL)
            txt_id.delete(0, 'end')
            txt_id.insert(0, selecionar_ultimo_id()+1)
            txt_id.config(state=DISABLED)

def alterar(id, titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio):
    if titulo == '' or tecnica == '' or acuracia == '' or precisao == '' or desafio == '' or base_dados == '' or  deficiencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos.')
        
    else:
        try:
            db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Tamanda010203',
            database = 'testes'
            )
        
            cursor = db.cursor()
            cursor.execute('UPDATE `testes`.`artigos` SET `titulo` = "%s", `data` = STR_TO_DATE("%s","%%Y-%%m-%%d"), `base_dados` = "%s", `tecnica` = "%s", `acuracia` = "%s", `precisao` = "%s", `deficiencia` = "%s", `desafio` = "%s" WHERE `id` = %s' %(titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio, id))
            db.commit()

            messagebox.showinfo('Sucesso', 'Registro alterado com sucesso.')

        except Exception as ex:
            messagebox.showwarning('Erro', ex)

        finally:
            db.close()
            carregar_tabela()

def excluir(id):
    try:
        db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'Tamanda010203',
        database = 'testes'
        )
        
        cursor = db.cursor()
        cursor.execute('DELETE FROM `testes`.`artigos` WHERE id = %s;' %(id))
        db.commit()

        messagebox.showinfo('Sucesso', 'Registro excluído com sucesso.')

    except Exception as ex:
        messagebox.showwarning('Erro', ex)

    finally:
        db.close()

def bloquear_botoes():
    btn_salvar_win.config(state=DISABLED)
    btn_alterar_win.config(state=DISABLED)
    btn_excluir.config(state=DISABLED)

def desbloquear_botoes(janela):
    btn_salvar_win.config(state=NORMAL)
    btn_alterar_win.config(state=NORMAL)
    btn_excluir.config(state=NORMAL)
    janela.destroy()

def reg_window(tipo, dgv_artigos):
    bloquear_botoes()

    reg_window = tk.Toplevel()
    reg_window.title('ADICIONAR ARTIGOS')
    reg_window.wm_protocol('WM_DELETE_WINDOW', lambda:desbloquear_botoes(reg_window))

    if len(dgv_artigos.get_children()) == 0 and not tipo:
        messagebox.showwarning('Erro', 'Cadastre um item.')
        desbloquear_botoes(reg_window)
        return

    lbl_id = tk.Label(reg_window, text='ID:')
    lbl_id.grid(column=0, row=0, padx=3, pady=3, sticky='W')

    txt_id = tk.Entry(reg_window, width=5)
    txt_id.grid(column=0, row=1, padx=3, pady=3, sticky='NW')

    lbl_titulo = tk.Label(reg_window, text='Título:')
    lbl_titulo.grid(column=1, row=0, padx=3, pady=3, sticky='W')

    txt_titulo = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_titulo.grid(column=1, row=1, padx=3, pady=3, sticky='NW')

    lbl_data = tk.Label(reg_window, text='Data:')
    lbl_data.grid(column=2, row=0, padx=3, pady=3, sticky='W')

    dtp_data = DateEntry(reg_window, selectmode='day')
    dtp_data.grid(column=2, row=1, padx=3, pady=3, sticky='NW')

    lbl_base_dados = tk.Label(reg_window, text='Base de Dados:')
    lbl_base_dados.grid(column=0, row=2, padx=3, pady=3, sticky='W')

    txt_base_dados = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_base_dados.grid(column=0, row=3, padx=3, pady=3, sticky='NW')

    lbl_tecnica = tk.Label(reg_window, text='Técnica Utilizada:')
    lbl_tecnica.grid(column=1, row=2, padx=3, pady=3, sticky='W')

    txt_tecnica = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_tecnica.grid(column=1, row=3, padx=3, pady=3, sticky='NW')

    lbl_acuracia = tk.Label(reg_window, text='Acurácia:')
    lbl_acuracia.grid(column=2, row=2, padx=3, pady=3, sticky='W')

    txt_acuracia = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_acuracia.grid(column=2, row=3, padx=3, pady=3, sticky='NW')

    lbl_precisao = tk.Label(reg_window, text='Previsão:')
    lbl_precisao.grid(column=0, row=4, padx=3, pady=3, sticky='W')

    txt_precisao = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_precisao.grid(column=0, row=5, padx=3, pady=3, sticky='NW')

    lbl_deficiencia = tk.Label(reg_window, text='Deficiência:')
    lbl_deficiencia.grid(column=1, row=4, padx=3, pady=3, sticky='W')

    txt_deficiencia = tk.Entry(reg_window, width=25, justify=LEFT)
    txt_deficiencia.grid(column=1, row=5, padx=3, pady=3, sticky='NW')

    lbl_desafio = tk.Label(reg_window, text='Desafio:')
    lbl_desafio.grid(column=2, row=4, padx=3, pady=3, sticky='W')

    txt_desafio = tk.Entry(reg_window, width=25)
    txt_desafio.grid(column=2, row=5, padx=3, pady=3, sticky='NW')

    if tipo:
        btn_salvar = tk.Button(reg_window, text='Salvar', width=10, height=1, command=lambda: salvar(txt_titulo.get(), str(dtp_data.get_date()), txt_base_dados.get(), txt_tecnica.get(), txt_acuracia.get(), txt_precisao.get(), txt_deficiencia.get(), txt_desafio.get(), txt_id))
        btn_salvar.grid(column=2, row=6, padx=3, pady=3, sticky='SE')
        
        txt_id.delete(0, 'end')
        txt_id.insert(0, selecionar_ultimo_id()+1)
        txt_id.config(state=DISABLED)
        
    else:
        btn_alterar = tk.Button(reg_window, text='Alterar', width=10, height=1, command=lambda: alterar(selecionar_id(), str(dtp_data.get_date()), dtp_data.get_date(), txt_base_dados.get(), txt_tecnica.get(), txt_acuracia.get(), txt_precisao.get(), txt_deficiencia.get(), txt_desafio.get()))
        btn_alterar.grid(column=2, row=6, padx=3, pady=3, sticky='SE')

        txt_id.delete(0, 'end')
        txt_id.insert(0, selecionar_id())
        txt_id.config(state=DISABLED)

        escrever_textbox(txt_titulo, dtp_data, txt_base_dados, txt_tecnica, txt_acuracia, txt_precisao, txt_deficiencia, txt_desafio)
        
window = tk.Tk()
window.title('ARTIGOS')

dgv_artigos = Treeview(window)
criar_tabela()
dgv_artigos.grid(column=0, row=0, padx=3, pady=3, sticky='N')

scroll = tk.Scrollbar(window, orient='vertical', command=dgv_artigos.yview)
scroll.grid(column=1, row=0, sticky='N')

dgv_artigos.configure(xscrollcommand = scroll.set)
carregar_tabela()

btn_salvar_win = tk.Button(window, text='Registrar\nNovo', width=10, height=2, command=lambda: reg_window(True, dgv_artigos))
btn_salvar_win.grid(column=0, row=1, padx=3, pady=3, sticky='SW')

btn_alterar_win = tk.Button(window, text='Alterar\nSelecionado', width=10, height=2, command=lambda: reg_window(False, dgv_artigos))
btn_alterar_win.grid(column=0, row=1, padx=3, pady=3, sticky='S')

btn_excluir = tk.Button(window, text='Excluir\nSelecionado', width=10, height=2, command=lambda: excluir(selecionar_id()))
btn_excluir.grid(column=0, row=1, padx=3, pady=3, sticky='SE')

window.mainloop()
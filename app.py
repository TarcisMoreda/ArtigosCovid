import tkinter as tk
import datetime
import xlsxwriter
import pickle

from tkinter.ttk import *
from tkinter.constants import DISABLED, END, NORMAL
from tkinter import messagebox
from tkcalendar import *

try:
    arquivo = open('db.dat', 'rb')
    print(pickle.load(arquivo))

except:
    arquivo = open('db.dat', 'wb')
    pickle.dump([], arquivo)

finally:
    arquivo.close()

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
        arquivo = open('db.dat', 'rb')
        dict_arquivo = pickle.load(arquivo)

        for row in dict_arquivo:
            dgv_artigos.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    except Exception as ex:
            messagebox.showwarning('Erro', ex)

    finally:
        arquivo.close()

def selecionar_id():
    try:
        item_atual = dgv_artigos.focus()
        return (dgv_artigos.item(item_atual).get('values')[0])

    except:
        messagebox.showwarning('Erro', 'Selecione um item da lista.')
        return 0

def selecionar_ultimo_id():
    try:
        if len(dgv_artigos.get_children()) != 0:
            ultimo = dgv_artigos.get_children()[-1]
            return (int(dgv_artigos.item(ultimo).get('values')[0]))
        
        else:
            return 0

    except Exception as ex:
        messagebox.showwarning('Erro', ex)

def escrever_textbox(id, titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio):
    try:
        item_atual = dgv_artigos.focus()
        tudo = dgv_artigos.item(item_atual).get('values')
        data_formatada = datetime.datetime.strptime(str(tudo[2]), '%Y-%m-%d').strftime('%d/%m/%Y')

        id.config(state=NORMAL)
        id.delete(0, 'end')
        id.insert(0, selecionar_id())
        id.config(state=DISABLED)

        titulo.insert(END, tudo[1])
        data.set_date(data_formatada)
        base_dados.insert(END, tudo[3])
        tecnica.insert(END, tudo[4])
        acuracia.insert(END, tudo[5])
        precisao.insert(END, tudo[6])
        deficiencia.insert(END, tudo[7])
        desafio.insert(END, tudo[8])
    
    except Exception as ex:
            messagebox.showwarning('Erro', ex)

def bloquear_botoes():
    btn_salvar_win.config(state=DISABLED)
    btn_alterar_win.config(state=DISABLED)
    btn_excluir.config(state=DISABLED)
    btn_pesquisar.config(state=DISABLED)
    btn_limpar.config(state=DISABLED)
    btn_exportar.config(state=DISABLED)

def desbloquear_botoes(janela):
    btn_salvar_win.config(state=NORMAL)
    btn_alterar_win.config(state=NORMAL)
    btn_excluir.config(state=NORMAL)
    btn_pesquisar.config(state=NORMAL)
    btn_limpar.config(state=NORMAL)
    btn_exportar.config(state=NORMAL)
    janela.destroy()

def limpar_campos(titulo, base_dados, tecnica, acuracia, precisao, deficiencia, desafio):
    titulo.delete("1.0", "end")
    base_dados.delete("1.0", "end")
    tecnica.delete("1.0", "end")
    acuracia.delete(0, 'end')
    precisao.delete(0, 'end')
    deficiencia.delete("1.0", "end")
    desafio.delete("1.0", "end")

def salvar(id, titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio, txt_id, txt_titulo, txt_base_dados, txt_tecnica, txt_acuracia, txt_precisao, txt_deficiencia, txt_desafio):
    if titulo == '' or tecnica == '' or acuracia == '' or precisao == '' or desafio == '' or base_dados == '' or  deficiencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos.')

    else:
        try:
            dict_artigo = [
                id,
                titulo,
                data,
                base_dados,
                tecnica,
                acuracia,
                precisao,
                deficiencia,
                desafio
            ]

            arquivo = open('db.dat', 'rb')
            dict_arquivo = pickle.load(arquivo)
            arquivo.close()
            
            dict_arquivo.append(dict_artigo)

            arquivo = open('db.dat', 'wb')
            pickle.dump(dict_arquivo, arquivo)

            messagebox.showinfo('Sucesso', 'Registrado com sucesso ao banco de dados.')

        except Exception as ex:
            messagebox.showwarning('Erro', ex)

        finally:
            arquivo.close()
            carregar_tabela()
            
            txt_id.config(state=NORMAL)
            txt_id.delete(0, 'end')
            txt_id.insert(0, selecionar_ultimo_id()+1)
            txt_id.config(state=DISABLED)

            limpar_campos(txt_titulo, txt_base_dados, txt_tecnica, txt_acuracia, txt_precisao, txt_deficiencia, txt_desafio)

def alterar(id, titulo, data, base_dados, tecnica, acuracia, precisao, deficiencia, desafio, janela):
    if id == 0:
        janela.destroy()
    
    if titulo == '' or tecnica == '' or acuracia == '' or precisao == '' or desafio == '' or base_dados == '' or  deficiencia == '':
        messagebox.showwarning('Erro', 'Preencha todos os campos.')
        
    else:
        try:
            dict_artigo = [
                id,
                titulo,
                data,
                base_dados,
                acuracia,
                precisao,
                deficiencia,
                desafio
            ]

            arquivo = open('db.dat', 'rb')
            dict_arquivo = pickle.load(arquivo)
            arquivo.close()

            arquivo = open('db.dat', 'wb')

            for i in dict_arquivo:
                if dict_artigo[0] == i[0]:
                    index = dict_arquivo.index(i)
                    dict_arquivo[index] = dict_artigo

            pickle.dump(dict_arquivo, arquivo)

            messagebox.showinfo('Sucesso', 'Registro alterado com sucesso.')

        except Exception as ex:
            messagebox.showwarning('Erro', ex)

        finally:
            arquivo.close()
            carregar_tabela()
            desbloquear_botoes(janela)

def excluir(id):
    if id == 0:
        return

    try:
        arquivo = open('db.dat', 'wrb')
        dict_arquivo = pickle.load(arquivo)

        for registros in dict_arquivo:
                if dict_arquivo[registros].get('ID') == id:
                    dict_arquivo[registros].pop()

        messagebox.showinfo('Sucesso', 'Registro excluído com sucesso.')

    except Exception as ex:
        messagebox.showwarning('Erro', ex)

    finally:
        arquivo.close()
        carregar_tabela()

def pesquisar(termo, coluna):
    resultado = []
    carregar_tabela()

    if coluna != 0 and termo != '':
        for child in dgv_artigos.get_children():
            if str(termo) in str(dgv_artigos.item(child)['values'][coluna-1]):
                resultado.append(dgv_artigos.item(child)['values'])

    else:
        messagebox.showwarning('Erro', 'Selecione uma coluna para ser pesquisada ou preencha o termo de pesquisa.')

    if resultado == []:
        messagebox.showinfo('Oops', 'Não existe um registro com esse valor.')

    else:
        dgv_artigos.delete(*dgv_artigos.get_children())
        
        for row in resultado:
            dgv_artigos.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

def limpar_pesquisa():
    txt_termo.delete(0, 'end')
    carregar_tabela()

def exportar_excel():
    wb = xlsxwriter.Workbook('Artigos.xlsx')
    ws = wb.add_worksheet()
    row = 2

    ws.write(0, 0, 'Artigos:')

    ws.write(1, 0, 'ID:')
    ws.write(1, 1, 'Título:')
    ws.write(1, 2, 'Data:')
    ws.write(1, 3, 'Base de Dados:')
    ws.write(1, 4, 'Técnica:')
    ws.write(1, 5, 'Acuracia:')
    ws.write(1, 6, 'Precisão:')
    ws.write(1, 7, 'Deficiência:')
    ws.write(1, 8, 'Desafio:')

    for artigo in dgv_artigos.get_children():
        for col in range(9):
            ws.write(row, col, dgv_artigos.item(artigo)['values'][col])

        row += 1

    wb.close()

def reg_window(tipo, dgv_artigos):
    bloquear_botoes()

    reg_window = tk.Toplevel()
    reg_window.title('ADICIONAR ARTIGOS')
    reg_window.wm_protocol('WM_DELETE_WINDOW', lambda:desbloquear_botoes(reg_window))

    if len(dgv_artigos.get_children()) == 0 and not tipo:
        messagebox.showwarning('Erro', 'Cadastre um item.')
        desbloquear_botoes(reg_window)

    if not tipo:
        try:
            dgv_artigos.item(dgv_artigos.focus()).get('values')[0]
    
        except:
            messagebox.showwarning('Erro', 'Selecione um item.')
            desbloquear_botoes(reg_window)

    lbl_id = tk.Label(reg_window, text='ID:')
    lbl_id.grid(column=0, row=0, padx=3, pady=3, sticky='W')

    txt_id = tk.Entry(reg_window, width=5, state=DISABLED)
    txt_id.grid(column=0, row=1, padx=3, pady=3, sticky='NW')

    lbl_data = tk.Label(reg_window, text='Data:')
    lbl_data.grid(column=1, row=0, padx=3, pady=3, sticky='W')

    dtp_data = DateEntry(reg_window, selectmode='day')
    dtp_data.grid(column=1, row=1, padx=3, pady=3, sticky='NSEW')

    lbl_acuracia = tk.Label(reg_window, text='Acurácia:')
    lbl_acuracia.grid(column=2, row=0, padx=3, pady=3, sticky='W')

    txt_acuracia = tk.Entry(reg_window, width=25)
    txt_acuracia.grid(column=2, row=1, padx=3, pady=3, sticky='NSEW')

    lbl_precisao = tk.Label(reg_window, text='Precisão:')
    lbl_precisao.grid(column=3, row=0, padx=3, pady=3, sticky='W')

    txt_precisao = tk.Entry(reg_window, width=25)
    txt_precisao.grid(column=3, row=1, padx=3, pady=3, sticky='NSEW')

    lbl_titulo = tk.Label(reg_window, text='Título:')
    lbl_titulo.grid(column=0, row=2, padx=3, pady=3, sticky='W')

    txt_titulo = tk.Text(reg_window, width=100, height=5)
    txt_titulo.grid(column=0, row=3, padx=3, pady=3, sticky='NW', columnspan=4)

    lbl_base_dados = tk.Label(reg_window, text='Base de Dados:')
    lbl_base_dados.grid(column=0, row=4, padx=3, pady=3, sticky='W')

    txt_base_dados = tk.Text(reg_window, width=100, height=5)
    txt_base_dados.grid(column=0, row=5, padx=3, pady=3, sticky='NW', columnspan=4)

    lbl_tecnica = tk.Label(reg_window, text='Técnica Utilizada:')
    lbl_tecnica.grid(column=0, row=6, padx=3, pady=3, sticky='W')

    txt_tecnica = tk.Text(reg_window, width=100, height=5)
    txt_tecnica.grid(column=0, row=7, padx=3, pady=3, sticky='NW', columnspan=4)

    lbl_deficiencia = tk.Label(reg_window, text='Deficiência:')
    lbl_deficiencia.grid(column=0, row=8, padx=3, pady=3, sticky='W')

    txt_deficiencia = tk.Text(reg_window, width=100, height=5)
    txt_deficiencia.grid(column=0, row=9, padx=3, pady=3, sticky='NW', columnspan=4)

    lbl_desafio = tk.Label(reg_window, text='Desafio:')
    lbl_desafio.grid(column=0, row=10, padx=3, pady=3, sticky='W')

    txt_desafio = tk.Text(reg_window, width=100, height=5)
    txt_desafio.grid(column=0, row=11, padx=3, pady=3, sticky='NW', columnspan=4)

    if tipo:
        btn_salvar = tk.Button(reg_window, text='Salvar', width=10, height=2, command=lambda: salvar(txt_id.get(), txt_titulo.get("1.0",'end-1c'), str(dtp_data.get_date()), txt_base_dados.get("1.0",'end-1c'), txt_tecnica.get("1.0",'end-1c'), txt_acuracia.get(), txt_precisao.get(), txt_deficiencia.get("1.0",'end-1c'), txt_desafio.get("1.0",'end-1c'), 
                                                                                                     txt_id, txt_titulo, txt_base_dados, txt_tecnica, txt_acuracia, txt_precisao, txt_deficiencia, txt_desafio))
        btn_salvar.grid(column=0, row=13, padx=3, pady=3, sticky='NSEW', columnspan=4, rowspan=2)
        
        txt_id.config(state=NORMAL)
        txt_id.delete(0, 'end')
        txt_id.insert(0, selecionar_ultimo_id()+1)
        txt_id.config(state=DISABLED)
        
    else:
        btn_alterar = tk.Button(reg_window, text='Alterar', width=10, height=2, command=lambda: alterar(selecionar_id(), txt_titulo.get("1.0",'end-1c'), str(dtp_data.get_date()), txt_base_dados.get("1.0",'end-1c'), txt_tecnica.get("1.0",'end-1c'), txt_acuracia.get(), txt_precisao.get(), txt_deficiencia.get("1.0",'end-1c'), txt_desafio.get("1.0",'end-1c'), reg_window))
        btn_alterar.grid(column=0, row=13, padx=3, pady=3, sticky='NSEW', columnspan=4, rowspan=2)

        txt_id.config(state=NORMAL)
        txt_id.delete(0, 'end')
        txt_id.insert(0, selecionar_id())
        txt_id.config(state=DISABLED)

        escrever_textbox(txt_id, txt_titulo, dtp_data, txt_base_dados, txt_tecnica, txt_acuracia, txt_precisao, txt_deficiencia, txt_desafio)
        
window = tk.Tk()
window.title('ARTIGOS')

lbl_termo = tk.Label(window, text='Termo de Pesquisa:')
lbl_termo.grid(column=0, row=0, padx=3, pady=3, sticky='W')

txt_termo = tk.Entry(window, width=25)
txt_termo.grid(column=0, row=1, padx=3, pady=3, sticky='NSEW')

lbl_pesquisa = tk.Label(window, text='Coluna pesquisada:')
lbl_pesquisa.grid(column=1, row=0, padx=3, pady=3, sticky='W')

cbb_pesquisa = Combobox(window, width=25, values=['', 'ID', 'Título', 'Data', 'Base de Dados', 'Técnica', 'Acurácia', 'Precisão', 'Deficiência', 'Desafio'])
cbb_pesquisa.grid(column=1, row=1, padx=2.5, pady=3, sticky='NSEW')

btn_pesquisar = tk.Button(window, text='Pesquisar', width=10, height=2, command=lambda:pesquisar(txt_termo.get(), cbb_pesquisa.current()))
btn_pesquisar.grid(column=2, row=0, padx=10, pady=3, sticky='NSW', rowspan=2)

btn_limpar = tk.Button(window, text='Limpar\nPesquisa', width=10, height=2, command=limpar_pesquisa)
btn_limpar.grid(column=2, row=0, padx=10, pady=3, sticky='NSE', rowspan=2)

dgv_artigos = Treeview(window)
criar_tabela()
dgv_artigos.grid(column=0, row=2, padx=3, pady=3, sticky='N', columnspan=3)

scroll = tk.Scrollbar(window, orient='vertical', command=dgv_artigos.yview)
scroll.grid(column=2, row=2, sticky='NSE', pady=3)
dgv_artigos.configure(yscrollcommand = scroll.set)

carregar_tabela()

btn_salvar_win = tk.Button(window, text='Registrar\nNovo', width=10, height=2, command=lambda: reg_window(True, dgv_artigos))
btn_salvar_win.grid(column=0, row=3, padx=3, pady=3, sticky='NSEW')

btn_alterar_win = tk.Button(window, text='Alterar\nSelecionado', width=10, height=2, command=lambda: reg_window(False, dgv_artigos))
btn_alterar_win.grid(column=1, row=3, padx=3, pady=3, sticky='NSEW')

btn_excluir = tk.Button(window, text='Excluir\nSelecionado', width=10, height=2, command=lambda: excluir(selecionar_id()))
btn_excluir.grid(column=2, row=3, padx=3, pady=3, sticky='NSEW')

btn_exportar = tk.Button(window, text='Exportar itens atuais para tabela do Excel', width=10, height=2, command=exportar_excel)
btn_exportar.grid(column=0, row=4, padx=3, pady=3, columnspan=4, sticky='NSEW')

window.mainloop()
import os  # Biblioteca para manipulação de arquivos e diretórios
import tkinter as tk  # Biblioteca para interface gráfica
from tkinter import filedialog, simpledialog, messagebox  # Importando ferramentas específicas para interação com o usuário

# Função para renomear arquivos em um diretório específico
def renomear_arquivos(pasta, trecho_remover):
    if not os.path.exists(pasta):  # Verifica se a pasta informada existe
        messagebox.showerror("Erro", "O diretório não existe!")  # Exibe uma mensagem de erro caso a pasta não seja encontrada
        return  # Sai da função para evitar erros
    
    arquivos_renomeados = 0  # Contador para rastrear quantos arquivos foram renomeados
    
    for filename in os.listdir(pasta):  # Lista todos os arquivos dentro da pasta fornecida
        novo_nome = filename.replace(trecho_remover, "").strip()  # Remove o trecho desejado do nome do arquivo e elimina espaços extras
        antigo_caminho = os.path.join(pasta, filename)  # Caminho completo do arquivo original
        novo_caminho = os.path.join(pasta, novo_nome)  # Caminho completo do novo arquivo renomeado
        
        if antigo_caminho != novo_caminho:  # Verifica se há mudança no nome para evitar renomeações desnecessárias
            os.rename(antigo_caminho, novo_caminho)  # Renomeia o arquivo
            arquivos_renomeados += 1  # Incrementa o contador
    
    # Exibe uma mensagem informando quantos arquivos foram modificados
    messagebox.showinfo("Concluído", f"Renomeação concluída! {arquivos_renomeados} arquivos foram modificados.")

# Função para pedir ao usuário que selecione uma pasta e insira o termo a ser removido
def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta com os arquivos")  # Abre um seletor de diretório
    if pasta:  # Se o usuário escolheu uma pasta válida
        termo = simpledialog.askstring("Entrada", "Qual termo deseja remover dos nomes dos arquivos?")  # Pede ao usuário o termo a ser removido
        if termo:  # Se o usuário inseriu um termo válido
            renomear_arquivos(pasta, termo)  # Chama a função para renomear os arquivos

# Criando a interface gráfica
root = tk.Tk()  # Inicializa a aplicação Tkinter
root.withdraw()  # Oculta a janela principal, pois usaremos apenas diálogos
selecionar_pasta()  # Chama a função principal para iniciar o processo

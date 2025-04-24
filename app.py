import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yaml
import subprocess
from pathlib import Path
import csv

CONFIG_FILE = "config.yaml"
processo = None  # Variável global para armazenar o processo em execução

def mostrar_relatorio_em_tabela(caminho):
    janela = tk.Toplevel()
    janela.title("Relatório de Contagem")
    janela.geometry("800x400")

    with open(caminho, newline='', encoding="utf-8") as f:
        leitor = csv.reader(f)
        linhas = list(leitor)

    if not linhas:
        tk.Label(janela, text="Relatório vazio.").pack()
        return

    colunas = linhas[0]
    tree = ttk.Treeview(janela, columns=colunas, show="headings")

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor='center')

    for linha in linhas[1:]:
        tree.insert("", "end", values=linha)

    tree.pack(expand=True, fill="both")

def escolher_video():
    global processo
    caminho = filedialog.askopenfilename(filetypes=[("Vídeos MP4", "*.mp4")])
    if not caminho:
        return

    # Atualiza o config.yaml
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)
    config["video_path"] = caminho
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(config, f)

    messagebox.showinfo("Etapa 1", "Vídeo carregado com sucesso! Agora vamos definir a linha de contagem.")
    subprocess.run(["python", "draw_line_config.py"])

    messagebox.showinfo("Etapa 2", "Linha definida! Agora selecione a região do semáforo.")
    subprocess.run(["python", "draw_traffic_light_config.py"])

    messagebox.showinfo("Etapa 3", "Semáforo definido! Agora vamos processar o vídeo.")
    subprocess.run(["python", "main.py"])

    # Mostra os resultados finais como tabela
    relatorio_path = Path("relatorios/relatorio.csv")
    if relatorio_path.exists():
        mostrar_relatorio_em_tabela(relatorio_path)
        messagebox.showinfo("Relatório Gerado", f"Relatório salvo em: {relatorio_path.resolve()}\n\nResumo:\n{conteudo}")
    else:
        messagebox.showerror("Erro", "Relatório não encontrado.")

def interromper_execucao():
    global processo
    if processo:
        processo.terminate()
        messagebox.showinfo("Execução Interrompida", "A execução foi interrompida com sucesso.")

def sair_app(root):
    root.quit()

def iniciar_app():
    root = tk.Tk()
    root.title("Contador de Veículos com Semáforo")
    root.geometry("400x300")

    label = tk.Label(root, text="Selecione um vídeo para análise:", font=("Arial", 12))
    label.pack(pady=20)

    btn = tk.Button(root, text="Selecionar vídeo e iniciar análise", command=escolher_video, font=("Arial", 12))
    btn.pack(pady=10)

    interromper_btn = tk.Button(root, text="Interromper Execução", command=interromper_execucao, font=("Arial", 12))
    interromper_btn.pack(pady=10)

    sair_btn = tk.Button(root, text="Sair", command=lambda: sair_app(root), font=("Arial", 12))
    sair_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()
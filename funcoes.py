from deck_lib import *

def seleciona_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Selecione um arquivo CSV"
    )
    if caminho_arquivo:
        processa_arquivo(caminho_arquivo)

def processa_arquivo(caminho_arquivo):
    try:
        texto_processado.configure(state="normal")
        texto_processado.delete("1.0",END)
        df = pd.read_csv(caminho_arquivo)
        for i in range(len(df)):
            if df["Deck Card Type"][i] == "Main":
                print(df['Quantity'][i],df["Name"][i])
                texto_processado.insert('1.0',f"{df['Quantity'][i]} {df['Name'][i]}\n")
        texto_processado.configure(state='disabled')  

    except Exception as e:
        messagebox.showerror("Erro",f"não foi possivel carregar o arquivo {e}")

def copiar():
    janela.clipboard_clear()
    janela.clipboard_append(texto_processado)
    janela.update()

def cria_janela():
    global janela
    global texto_processado
    
    janela = Tk()
    janela.title("Deck lister")

    texto_orientação = Label(janela,text="Clique no botao para ver a cotação das moedas")
    texto_orientação.grid(column=0 , row=0)

    botao = Button(janela,text="Selecione o arquivo",command=seleciona_arquivo)
    botao.grid(column=0,row=1)

    texto_processado = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=20, height=20)
    texto_processado.grid(column=0, row=2)
    texto_processado.configure(state='disabled') 

    botao_copiar = Button(janela,text="Copiar",command=copiar)
    botao_copiar.grid(column=0,row=3)

    janela.mainloop()
    
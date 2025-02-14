#coding: utf-8
import tkinter as tk
import sqlite3 as sq #Importacao do banco de dados. 

def CriacaoBancoDados(): 
	NomeBD = "Usuario_senha.db"
	tabelaBD = '''
		CREATE TABLE IF NOT EXISTS Usuario_senha(
			nome TEXT NOT NULL,
			senha TEXT NOT NULL);
			'''
	conexao = sq.connect(NomeBD)
	cursor = conexao.cursor()
	cursor.execute(tabelaBD)
	conexao.commit()
	nome = input("Digite seu nome: ")
	senha = input("Digite sua senha: ")
	conexao.execute("INSERT INTO Usuario_senha VALUES (?,?)", (nome, senha))
	conexao.commit()
	
	
			


class Controlador(tk.Frame):
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		#Chama uma outra classe para construir a pagina sobre a pagina pai.
		self.PagLogin = PaginaLogin(self)
		self.PagLogin.grid(row=0, column = 0)
		
		#Criacao do menu de tela. 
		self.menu = TrocadorTela(self)
		self.menu.grid(row = 1, column = 0)
		

class TrocadorTela(tk.Frame): 
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		#Cuidado com o comando
		self.PagLogin = tk.Button(self, text = "Login", height = 2, width = 16, command = self.master.PagLogin.tkraise)			
		self.PagLogin.grid(row = 0, column = 0)
		

class PaginaLogin(tk.Frame): 
	def __init__(self, JanPr): 
		tk.Frame.__init__(self,JanPr)
		#Colocar um label para iniciar a tela de login
		self.Label1=tk.Label(self, text = "Tela de Login", height = 5, width = 40, 
			background = "Green")
		self.Label1.grid(row = 0, column = 0)
		#Colocacao de nome de usuario e senha: 
		self.Label_Nome_usuario = tk.Label(self, text = "Nome do usuario: ", 
			height= 3, width = 15)
		self.Label_Nome_usuario.grid(row=1, column = 0)
		self.Entry_Nome_usuario=tk.Entry(self)
		self.Entry_Nome_usuario.grid(row=1, column = 1)
		self.Label_Senha_usuario = tk.Label(self, text = "Senha do usuario: ", 
			height= 3, width = 15)
		self.Label_Senha_usuario.grid(row=2, column = 0)
		self.Entry_Senha_usuario=tk.Entry(self, show = "*")
		self.Entry_Senha_usuario.grid(row=2, column = 1)
		#colocaco do botao
		self.VerLogin = tk.Button(self, text = "Entrar", bg = "White", height = 2, 
			width = 15, command = self.VerificaLogin)
		self.VerLogin.grid(row = 3, column=0)	
	
	def VerificaLogin(self): 
		print("Entrou")		
		conexao = sq.connect('Usuario_senha.db')
		cursor=conexao.cursor()
		Selecao = '''
			SELECT * FROM Usuario_senha
			'''
		cursor.execute(Selecao)	
		Dados = cursor.fetchall()
		print(Dados)
		
		
		



			




def main(): 	
	JanelaPrincipal = tk.Tk()
	JanelaPrincipal.title("Banco Python")
	#Criacao de janela com 70% do tamanho da tela. 
	TamHorJanela = int(JanelaPrincipal.winfo_screenwidth()*0.3)
	TamVertJanela = int(JanelaPrincipal.winfo_screenheight()*0.6)
	print(TamHorJanela, TamVertJanela)
	TamTela = str(TamHorJanela)+"x"+str(TamVertJanela)
	JanelaPrincipal.geometry(TamTela)
	Pagina0 = Controlador(JanelaPrincipal)
	Pagina0.pack(expand = True, fill=tk.BOTH)
	JanelaPrincipal.mainloop()

if __name__=="__main__": 
	CriacaoBancoDados()
	main()
	




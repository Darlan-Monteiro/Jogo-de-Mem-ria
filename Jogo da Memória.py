import tkinter as tk
from tkinter import messagebox
import random

# Define o número de linhas e colunas
NUM_ROWS = 6
NUM_COLS = 6
CARD_SIZE_W = 10  # Define a largura de cada cartão
CARD_SIZE_H = 5   # Define a altura de cada cartão

# Define as cores dos cartões (18 cores diferentes para 36 cartões)
CARD_COLORS = [
    'red', 'blue', 'green', 'yellow', 'purple', 'orange', 
    'cyan', 'magenta', 'brown', 'pink', 'lime', 'grey', 
    'navy', 'teal', 'maroon', 'olive', 'violet', 'turquoise'
]

# Define outras constantes
BG_COLOR = '#343a40'
FONT_COLOR = 'white'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_ATTEMPTS = 40  # Número máximo de tentativas

def create_card_grid():
    colors = CARD_COLORS * 2  # Duplica a lista de cores para criar pares
    random.shuffle(colors)    # Embaralha as cores
    grid = []
    for _ in range(NUM_ROWS):
        row = []
        for _ in range(NUM_COLS):
            color = colors.pop()  # Remove uma cor do final da lista embaralhada
            row.append(color)     # Adiciona a cor à linha
        grid.append(row)          # Adiciona a linha à grade
    return grid

def card_clicked(row, col):
    card = cards[row][col]
    color = card['bg']
    if color == 'black':  # Verifica se o cartão está virado para baixo
        card['bg'] = grid[row][col]  # Revela a cor do cartão
        revealed_cards.append(card)
        if len(revealed_cards) == 2:  # Verifica se dois cartões foram revelados
            check_match()

def check_match():
    card1, card2 = revealed_cards
    if card1['bg'] == card2['bg']:  # Verifica se os cartões são iguais
        card1.after(1000, card1.destroy)
        card2.after(1000, card2.destroy)
        matched_cards.extend([card1, card2])
        check_win()
    else:
        card1.after(1000, lambda: card1.config(bg='black'))
        card2.after(1000, lambda: card2.config(bg='black'))
    revealed_cards.clear()
    update_score()

def check_win():
    if len(matched_cards) == NUM_ROWS * NUM_COLS:
        messagebox.showinfo('Parabéns!', 'Você venceu o jogo!')
        window.quit()

def update_score():
    global attempts
    attempts += 1
    attempts_label.config(text='Tentativas: {}/{}'.format(attempts, MAX_ATTEMPTS))
    if attempts >= MAX_ATTEMPTS:
        messagebox.showinfo('Fim de Jogo', 'Você perdeu o jogo!')
        window.quit()

# Cria a janela principal do jogo
window = tk.Tk()
window.title('Jogo de Memória')
window.configure(bg=BG_COLOR)  # Aqui define a cor de fundo da janela principal

# Cria a grade de cartões
grid = create_card_grid()
cards = []
revealed_cards = []
matched_cards = []
attempts = 0

# Cria os botões que representam os cartões
for row in range(NUM_ROWS):
    row_of_cards = []
    for col in range(NUM_COLS):
        card = tk.Button(window, width=CARD_SIZE_W, height=CARD_SIZE_H, bg='black',
                        relief=tk.RAISED, bd=3, command=lambda r=row, c=col: card_clicked(r, c))
        card.grid(row=row, column=col, padx=5, pady=5)
        row_of_cards.append(card)
    cards.append(row_of_cards)
    
# Define o estilo dos botões
button_style = {'activebackground': '#f8f9fa', 'font': FONT_STYLE, 'fg': FONT_COLOR}
window.option_add('*Button', button_style)

# Cria o rótulo de tentativas
attempts_label = tk.Label(window, text='Tentativas: {}/{}'.format(attempts, MAX_ATTEMPTS), fg=FONT_COLOR, bg=BG_COLOR, font=FONT_STYLE)
attempts_label.grid(row=NUM_ROWS, columnspan=NUM_COLS, padx=10, pady=10)  # Aqui define a cor de fundo da etiqueta de tentativas

# Inicia o loop principal da janela
window.mainloop()

import keyboard
from collections import defaultdict
import time

import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 5
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trajeto da Formiga")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Grid para rastrear o trajeto
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Classe para representar uma formiga
class Ant:
    def __init__(self, color, start_pos):
        self.color = color
        self.x, self.y = start_pos
        self.direction = random.choice([0, 1, 2, 3])  # 0: cima, 1: direita, 2: baixo, 3: esquerda

    def move(self):
        # Calcular próxima posição com base na direção
        dx, dy = 0, 0
        if self.direction == 0:
            dy = -1
        elif self.direction == 1:
            dx = 1
        elif self.direction == 2:
            dy = 1
        elif self.direction == 3:
            dx = -1

        # Verificar limites do grid
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < COLS and 0 <= new_y < ROWS:
            self.x, self.y = new_x, new_y
            grid[new_y][new_x] = 1  # Marcar o trajeto como preto

    def draw(self):
        # Desenhar a formiga em sua posição atual
        pygame.draw.rect(screen, self.color, 
                         (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Classe para representar a Formiga de Langton com múltiplas cores
class LangtonAntMultiColor:
    def __init__(self, colors, rules, start_pos):
        self.colors = colors  # Lista de cores
        self.rules = rules    # Sequência de "L" e "R"
        self.num_states = len(colors)  # Número de estados (cores)
        self.x, self.y = start_pos
        self.direction = 0  # 0: cima, 1: direita, 2: baixo, 3: esquerda

    def move(self):
        # Obter o estado atual da célula
        current_state = grid[self.y][self.x]

        # Aplicar a regra correspondente ao estado atual
        if self.rules[current_state] == "R":  # Virar à direita
            self.direction = (self.direction + 1) % 4
        elif self.rules[current_state] == "L":  # Virar à esquerda
            self.direction = (self.direction - 1) % 4

        # Atualizar o estado da célula (cíclico)
        grid[self.y][self.x] = (current_state + 1) % self.num_states

        # Calcular próxima posição com base na direção
        dx, dy = 0, 0
        if self.direction == 0:  # Cima
            dy = -1
        elif self.direction == 1:  # Direita
            dx = 1
        elif self.direction == 2:  # Baixo
            dy = 1
        elif self.direction == 3:  # Esquerda
            dx = -1

        # Verificar limites do grid
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < COLS and 0 <= new_y < ROWS:
            self.x, self.y = new_x, new_y

    def draw(self):
        # Desenhar a formiga em sua posição atual
        pygame.draw.rect(screen, self.colors[grid[self.y][self.x]], 
                         (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Definindo as cores e regras
color_options = {
    "RL": [(0, 0, 0), (255, 255, 255)],  # Preto e Branco
    "RRL": [(0, 0, 0), (255, 0, 0), (0, 0, 255)],  # Preto, Vermelho, Azul
    "RRLL": [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)],  # Preto, Vermelho, Verde, Azul
    "LRRRRRLLR": [(0, 0, 0), (128, 0, 128), (173, 216, 230), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)],  # Preto, Roxo, Azul Claro, Branco, Vermelho, Verde, Azul, Amarelo, Ciano
    "LLRRRLRLRLLR": [(0, 0, 0), (128, 0, 128), (173, 216, 230), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (192, 192, 192), (255, 105, 180), (139, 69, 19)],  # Adicionando Cinza, Rosa, Marrom
    "RRLLLRLLLRRR": [(0, 0, 0), (128, 0, 128), (173, 216, 230), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (75, 0, 130), (238, 130, 238), (255, 165, 0)],  # Adicionando Índigo, Violeta, Laranja
}

rule_options = {
    "RL": "RL",
    "RRL": "RRL",
    "RRLL": "RRLL",
    "LRRRRRLLR": "LRRRRRLLR",
    "LLRRRLRLRLLR": "LLRRRLRLRLLR",
    "RRLLLRLLLRRR": "RRLLLRLLLRRR",
}

# Adicionar nova sequência e cores com entrada do usuário
import random

def gerar_cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

nova_sequencia = input("Digite uma nova sequência de R e L (exemplo: RLRLRL): ").upper()

while not all(c in "RL" for c in nova_sequencia):
    print("A sequência deve conter apenas os caracteres 'R' e 'L'.")
    nova_sequencia = input("Digite uma nova sequência de R e L (exemplo: RLRLRL): ").upper()

nova_cor = [gerar_cor_aleatoria() for _ in nova_sequencia]

color_options["nova"] = nova_cor
rule_options["nova"] = nova_sequencia

# Escolher a nova sequência
selected_rule = "nova"
colors = color_options[selected_rule]
rules = rule_options[selected_rule]

# Criar uma única formiga de Langton com múltiplas cores
ant = LangtonAntMultiColor(colors, rules, (COLS // 2, ROWS // 2))

# Loop principal
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)  # Fundo preto
    
    # Atualizar e desenhar a formiga
    ant.move()
    ant.draw()
    
    # Desenhar o grid (trajeto)
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x] > 0:
                pygame.draw.rect(screen, colors[grid[y][x]], 
                                 (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    pygame.display.flip()
    clock.tick(120)  # Ajuste a velocidade de movimento

    # Eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

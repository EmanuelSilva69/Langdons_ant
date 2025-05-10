# Formiga de Langton com Múltiplas Cores em Python

## Visão Geral
Este projeto implementa a clássica Formiga de Langton usando o Pygame, onde a formiga pode seguir uma sequência específica de regras para mudar sua cor e direção ao se mover. A Formiga de Langton é um autômato celular simples que simula comportamentos complexos através de suas regras simples.

## Requisitos
- Python 3.x
- Pygame

## Instalação
Para instalar as dependências necessárias, execute o seguinte comando no terminal:
```
pip install pygame
```

## Funcionalidades
1. **Multiplas Cores**: A formiga pode assumir várias cores com base em seu estado atual e a sequência de regras aplicadas.
2. **Gerenciamento de Estado**: As células do grid podem estar em diferentes estados, cada um representado por uma cor.
3. **Sequências Personalizáveis**: O usuário pode definir sua própria sequência de regras (combinações de "R" e "L") para controlar o comportamento da formiga.

## Como Usar

### Passos Iniciais
- Execute o script Python fornecido.
- A janela do Pygame será exibida, onde a Formiga de Langton começará a se mover no grid preto.

### Definindo Novas Sequências e Cores
- O script permite ao usuário definir novas sequências de regras ("R" para direita e "L" para esquerda).
- Para cada nova sequência, uma cor aleatória será gerada e associada a um estado.
- Exemplo de entrada: 
  ```
  Digite uma nova sequência de R e L (exemplo: RLRLRL): RLRLLR
  ```

### Personalizando o Comportamento
- A sequência definida pelo usuário controlará como a formiga muda de cor e direção ao se mover.
- As cores associadas a cada estado permitem observar padrões interessantes na evolução do grid.

## Exemplos de Sequências

1. **RL**
   - A formiga muda de cor para preto em estados pares e para branco em estados ímpares, girando 90 graus à direita sempre.

2. **RRL**
   - A formiga usa três cores diferentes (preto, vermelho e azul) alternadamente, girando 90 graus à direita quando passa por um estado par e à esquerda quando passa por um estado ímpar.

3. **RRLL**
   - Quatro cores (preto, vermelho, verde e azul) são usadas em sequência, girando 90 graus à direita e à esquerda alternadamente.

## Considerações Finais
Este projeto é uma implementação simples da Formiga de Langton que demonstra como combinar regras básicas com cores para criar padrões complexos. O código é fácil de entender e pode ser modificado para explorar diferentes comportamentos interessantes.

Para mais informações sobre a Formiga de Langton, consulte o artigo original em [Wikipedia](https://en.wikipedia.org/wiki/Langton's_ant).

## Contribuições
Contribuções são bem-vindas! Se você encontrar qualquer bug ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
```
MIT License
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Esse README fornece uma visão geral do projeto, instruções de instalação, funcionalidades e como usar o código. Você pode ajustar conforme necessário para melhor se adequar às suas necessidades específicas.

------------------------------

![image](https://github.com/user-attachments/assets/3cc89a99-99d7-4eb3-9b3b-66ee5f24500c)
![image](https://github.com/user-attachments/assets/82e665e6-3f0b-4d58-8f3d-3da4ed3e2873)

![image](https://github.com/user-attachments/assets/b3601e03-43b3-4afa-a8d0-19f4bb9d7d7e)

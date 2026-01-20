# Python GUIs (Tkinter)

Coleção de exemplos simples de GUI com Tkinter (e Pillow para imagens), voltados a aprendizado básico.

## Requisitos

- Python 3
- Tkinter (já vem com a maioria das instalações do Python)
- Pillow (para abrir imagens): `pip install pillow`
- Arquivo de imagem `python.png` na mesma pasta dos scripts que usam imagem

## Como executar

Na pasta do projeto, rode:

- `python app1.py`
- `python button.py`
- `python checkbutton.py`
- `python frame.py`
- `python image.py`
- `python input+label.py`
- `python Label.py`
- `python messagebox.bind.py`
- `python messagebox.command.py`
- `python radiobutton.py`
- `python teste.py`
- `python void.py`

## Descrição de cada programa

- **app1.py**:
  - Cria uma janela com título e uma imagem carregada via Pillow (`Image.open` e `ImageTk.PhotoImage`).
  - Usa `Frame` para agrupar `Label` (Username) e `Entry` lado a lado (`pack` com `side=LEFT/RIGHT`).
  - Botão “Lets Start” posicionado na parte inferior (`pack` com `side=BOTTOM`).
  - Demonstra organização visual com `pack` e uso de `Frame`.

- **button.py**:
  - Exibe título, imagem, rótulo “Username” e `Entry` na janela principal.
  - Botão “Lets Start” posicionado com coordenadas absolutas usando `place(x=100, y=350)`.
  - Mostra a diferença entre `pack` e `place` no layout.

- **checkbutton.py**:
  - Texto introdutório e um `Frame` contendo múltiplos `Checkbutton`.
  - Opções: Python, Java, JavaScript e C++.
  - Exemplo simples de seleção múltipla (sem variáveis de estado explicitamente ligadas).

- **frame.py**:
  - Cria um `Frame` dentro da janela principal.
  - Adiciona um `Label` e um `Button` dentro do frame.
  - Demonstra como agrupar widgets para facilitar o layout.

- **image.py**:
  - Abre a imagem `python.png` com Pillow e exibe com `Label`.
  - Inclui um título estilizado (`font`, `bg`, `fg`).
  - Exemplo básico de imagem + texto.

- **input+label.py**:
  - Combina título, imagem e um par `Label` + `Entry`.
  - O rótulo “Username” fica à esquerda e o campo à direita (`pack` com `side`).
  - Demonstra composição de widgets e alinhamento simples.

- **Label.py**:
  - Exemplo mínimo com um único `Label` estilizado.
  - Demonstra uso de texto, cor de fundo/foreground e fonte.

- **messagebox.bind.py**:
  - Interface com título, imagem, `Frame` com rótulo e `Entry`.
  - O botão usa `bind('<Button-1>', ...)` para chamar uma função ao clicar.
  - A função lê o texto do `Entry` e atualiza um `Label` com “Welcome” + nome.
  - Demonstra eventos do Tkinter e atualização dinâmica de texto.

- **messagebox.command.py**:
  - Estrutura semelhante (título, imagem, `Frame`, `Entry`).
  - Botão usa `command=showMessage` para abrir `messagebox.showinfo`.
  - Função `gui()` organiza a criação da janela; `showMessage()` mostra a mensagem.
  - Exemplo de callbacks e uso de `messagebox`.

- **radiobutton.py**:
  - Exibe um rótulo “Gender” e dois `Radiobutton`.
  - Usa `StringVar()` para armazenar a seleção (`M` ou `F`).
  - Demonstra seleção exclusiva com `Radiobutton`.

- **teste.py**:
  - Imprime o caminho do Python em uso (`sys.executable`).
  - Verifica se o Pillow está instalado via `pkg_resources` e mostra a versão.
  - Útil para diagnosticar dependências.

- **void.py**:
  - Cria uma janela Tkinter vazia.
  - Exemplo mínimo de loop principal (`mainloop`).

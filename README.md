# RemoveTextRenamer

Este é um programa simples em Python para renomear arquivos dentro de um diretório, removendo um trecho específico do nome conforme definido pelo usuário. Ele foi criado para ajudar a padronizar nomes de arquivos, como no caso de ROMs de jogos, removendo partes indesejadas, como "(PT-BR)".

## Requisitos
- Python 3 instalado

## Instalação
1. Clone este repositório ou baixe os arquivos manualmente:
   ```sh
   git clone https://github.com/felipezardo/RemoveTextRenamer.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd RemoveTextRenamer
   ```
3. Instale as dependências necessárias (opcional, apenas se `tkinter` não estiver instalado):
   ```sh
   pip install tk
   ```

## Como usar?
1. Execute o script `RemoveTextRenamer.py`:
   ```sh
   python RemoveTextRenamer.py
   ```
2. Uma janela irá se abrir para você selecionar a pasta com os arquivos.
3. Depois de escolher a pasta, uma caixa de diálogo solicitará o termo a ser removido (exemplo: `(PT-BR)`).
4. O programa renomeará os arquivos dentro da pasta, removendo o trecho informado.
5. Uma mensagem de confirmação será exibida informando quantos arquivos foram renomeados.

## Explicação do código
O código segue uma estrutura simples:
1. Importa as bibliotecas `os` (para manipulação de arquivos) e `tkinter` (para interface gráfica).
2. Define a função `renomear_arquivos(pasta, trecho_remover)`, que percorre todos os arquivos da pasta e remove o trecho especificado do nome.
3. Cria a função `selecionar_pasta()`, que abre um seletor de diretório e uma caixa de entrada para o usuário digitar o trecho a ser removido.
4. Inicializa a interface do `tkinter`, oculta a janela principal e chama a função `selecionar_pasta()` para iniciar o processo.

## Observações
- O programa apenas remove o trecho do nome do arquivo, ele não adiciona nem modifica outras partes do nome.
- Se um arquivo já estiver com o nome final desejado, ele não será renomeado.
- Caso o diretório escolhido não contenha arquivos a serem modificados, nenhuma alteração será feita.

## Licença
Este projeto é de código aberto e pode ser usado livremente.

# RemoveTextRenamer

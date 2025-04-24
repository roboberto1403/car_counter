# 🚦 Sistema Inteligente de Contagem de Carros em um Semáforo

Este projeto implementa um sistema de contagem de veículos com base em vídeo, utilizando detecção automática (YOLOv5), reconhecimento de movimento e controle por semáforo. Ele permite ao usuário:

- Selecionar um vídeo local (.mp4)
- Definir uma linha virtual de contagem
- Selecionar a região do semáforo (ROI)
- Processar os dados automaticamente
- Gerar um relatório em formato `.csv` com os resultados

## 🔍 Objetivo

Criar uma ferramenta intuitiva e acessível para análise de trâfego, com interface gráfica e etapas visuais para auxiliar o usuário na definição da linha de contagem e da posição do semáforo.

---

## 🧰 Tecnologias utilizadas

- Python 3.8+
- OpenCV
- Tkinter (GUI)
- PyYAML
- YOLOv5 (pré-instalado)
- Pandas (para geração do relatório)

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

Você pode usar um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

E então:

```bash
pip install -r requirements.txt
```

> Se o arquivo `requirements.txt` não estiver criado, use:  
> `pip install opencv-python pyyaml pandas`  
> E instale o YOLOv5 seguindo as instruções no repositório oficial: https://github.com/ultralytics/yolov5

---

### 3. Execute o sistema

Clique no executável *app* localizado dentro da pasta *dist*

Você será guiado pelas seguintes etapas:

1. Escolha de um vídeo
2. Definição da linha de contagem
3. Seleção da região do semáforo
4. Processamento automático com geração de relatório

---

## 📄 Relatórios

Dois arquivos são gerados ao final da análise: `relatorio.csv` e `distribuicao_temporal.csv`.

- **relatorio.csv**: contém informações resumidas sobre o vídeo analisado, incluindo:

  - Nome do vídeo
  - Total de carros detectados
  - Tempo total em sinal verde e vermelho
  - Média de carros que passaram por ciclo verde
  - Taxa de passagem de carros por segundo

- **distribuicao\_temporal.csv**: apresenta dados detalhados por segundo, incluindo:

  - Tempo (em segundos)
  - Quantidade de carros detectados no frame
  - Estado do semáforo naquele instante

Os arquivos serão salvos na pasta:

```
relatorios/relatorio.csv
```

---

## 📌 Observações

- A definição da linha e da ROI do semáforo é interativa, com opção de corrigir antes de salvar.
- O código é modular e pode ser adaptado para novos cenários (semáforos múltiplos, diferentes modelos de detecção, etc).
- Sugestão de vídeo a ser utilizado: [link](https://www.pexels.com/video/busy-urban-traffic-flow-at-intersection-30609021/). 

---

## 🛠 Autor

**Luiz Roberto Bezerra Ferreira**  
[LinkedIn](https://linkedin.com/in/luiz-bferreira) | [GitHub](https://github.com/roboberto1403)

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://opensource.org/license/MIT).


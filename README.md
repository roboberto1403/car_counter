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

## 📄 Relatório

O relatório final será salvo na pasta:

```
relatorios/relatorio.csv
```

Este arquivo contém o número de veículos contados em diferentes estágios do semáforo (verde, amarelo, vermelho).

---

## 📌 Observações

- A definição da linha e da ROI do semáforo é interativa, com opção de corrigir antes de salvar.
- O código é modular e pode ser adaptado para novos cenários (semáforos múltiplos, diferentes modelos de detecção, etc).

---

## 🛠 Autor

**Luiz Roberto Bezerra Ferreira**  
[LinkedIn](https://linkedin.com/in/luiz-bferreira) | [GitHub](https://github.com/roboberto1403)

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://opensource.org/license/MIT).


# 🎮 Campus Run UFRPE

> Projeto desenvolvido para a disciplina de **Projeto Interdisciplinar de Sistemas de Informação** da Universidade Federal Rural de Pernambuco (UFRPE).

---

## 📖 Sobre o Jogo

**Campus Run UFRPE** é um jogo de plataforma 2D desenvolvido em Python utilizando a biblioteca Arcade. O jogador controla **Beto**, um estudante que precisa atravessar diferentes áreas do campus da UFRPE em um dia chuvoso, enfrentando obstáculos e desafios até alcançar seu destino final.

Durante a jornada, o personagem deve evitar veículos, superar obstáculos e coletar toalhas espalhadas pelo cenário para reduzir o nível de molhado causado pela chuva. Ao final da partida, o desempenho do jogador é avaliado com base no tempo de conclusão, quantidade de toalhas coletadas e condição final do personagem.

O projeto foi desenvolvido com fins acadêmicos para aplicar conceitos de programação, desenvolvimento de jogos digitais e trabalho colaborativo utilizando Git e GitHub.

---

## 🗺️ Cenário

O mapa do jogo foi inspirado em locais reais da Universidade Federal Rural de Pernambuco (UFRPE), proporcionando uma experiência próxima da vivenciada pelos estudantes.

Locais representados no jogo:

* 📍 Bar da Curva
* 📍 UFRPE (Sede Principal)
* 📍 DEINFO (Departamento de Estatística e Informática)
* 📍 CEAGRI II

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Arcade 3.x
* Pyglet
* Pillow
* Git
* GitHub

---

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/Campus-Run-UFRPE.git
cd Campus-Run-UFRPE
```

### 2. Criar o Ambiente Virtual

```bash
python -m venv .venv
```

### 3. Ativar o Ambiente Virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 4. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o Jogo

```bash
python main.py
```

---

## 🎮 Controles

| Tecla  | Função                |
| ------ | --------------------- |
| ⬅️     | Mover para a esquerda |
| ➡️     | Mover para a direita  |
| Espaço | Pular                 |

---

## 🏆 Sistema de Pontuação

Ao concluir a fase, a pontuação do jogador é calculada utilizando os seguintes critérios:

| Critério           | Peso |
| ------------------ | ---- |
| Tempo de conclusão | 50%  |
| Nível de molhado   | 30%  |
| Toalhas coletadas  | 20%  |

Quanto menor o tempo e o nível de molhado, e quanto maior a quantidade de toalhas coletadas, melhor será o desempenho final.

---

## 📸 Capturas de Tela

### 🏠 Tela Inicial

![Tela Inicial](screenshots/Campus%20Run_%20UFRPE%2017_06_2026%2023_53_48.png)

Tela inicial do jogo apresentando o personagem principal e o início da aventura pelo campus.

---

### 🏃 Gameplay

![Gameplay](screenshots/Campus%20Run_%20UFRPE%2017_06_2026%2023_54_18.png)

O jogador percorre o campus enfrentando desafios, desviando de obstáculos e coletando toalhas para permanecer seco.

---

### 🚗 Obstáculos e Desafios

![Obstáculos](screenshots/Campus%20Run_%20UFRPE%2017_06_2026%2023_54_58.png)

Os veículos presentes no cenário tornam a travessia mais difícil e exigem atenção constante do jogador.

---

### 🏆 Tela de Vitória

![Vitória](screenshots/voce_venceu.png)

Ao concluir o percurso com sucesso, o jogador recebe uma tela de vitória celebrando sua chegada ao destino final.

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para aplicar conhecimentos relacionados a:

* Programação Orientada a Objetos (POO)
* Desenvolvimento de Jogos 2D
* Estruturas de Dados
* Manipulação de Eventos
* Organização de Projetos Python
* Controle de Versão com Git
* Desenvolvimento Colaborativo com GitHub

---

## 👥 Equipe

Projeto desenvolvido por estudantes do curso de **Sistemas de Informação — UFRPE**.

* José Alberto
* Tomás Kavela

---

## 📄 Licença

Este projeto possui finalidade exclusivamente acadêmica e educacional, não sendo destinado a fins comerciais.

---

## 🎓 Universidade

Universidade Federal Rural de Pernambuco (UFRPE)

Disciplina: Projeto Interdisciplinar de Sistemas de Informação

Ano: 2026

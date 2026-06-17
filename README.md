# 🎮 Campus Run UFRPE

> Projeto desenvolvido para a disciplina de **Projeto Interdisciplinar de Sistemas de Informação** da Universidade Federal Rural de Pernambuco (UFRPE).

---

## 📖 Sobre o jogo

Campus Run UFRPE é um jogo de plataforma 2D onde o jogador controla **Beto**, um estudante que precisa atravessar o campus da UFRPE até o destino final sem se molhar completamente com a chuva.

Ao longo do caminho, Beto encontra veículos como obstáculos, pode coletar toalhas espalhadas pelo mapa para reduzir o nível de molhado, e é avaliado ao final por tempo, quantidade de toalhas coletadas e o quão seco chegou.

---

## 🗺️ Cenário

O mapa percorre pontos reais do campus, incluindo:

- **Bar da Curva**
- **UFRPE** (sede principal)
- **DEINFO** (Departamento de Estatística e Informática)
- **CEAGRI 2**

---

## ⚙️ Requisitos

- Python 3.11+
- [arcade](https://api.arcade.academy/) 3.x

---

## 🚀 Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/Campus-Run-UFRPE.git
cd Campus-Run-UFRPE
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Execute o jogo**
```bash
python main.py
```

---

## 🎮 Controles

| Tecla | Ação |
|---|---|
| `←` / `→` | Mover |
| `Espaço` | Pular |

---

## 🏆 Pontuação

A pontuação final é calculada com base em três fatores:

| Fator | Peso | Quanto melhor |
|---|---|---|
| Tempo | 50% | Mais rápido |
| Nível de molhado | 30% | Menos molhado |
| Toalhas coletadas | 20% | Mais toalhas |

---

## 👥 Equipe

Desenvolvido por estudantes do curso de **Sistemas de Informação — UFRPE**.
José Alberto e Tomás Kavela.

---

## 📄 Licença

Este projeto é de uso acadêmico e não possui fins comerciais.

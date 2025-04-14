# Projeto: Controle de LED com Python e Arduino

Este projeto integra Python com Arduino para controlar um LED usando uma interface gráfica. A comunicação é feita via porta serial (USB), utilizando a biblioteca `pyserial`. A interface, feita com `tkinter`, possui dois botões:

- **Piscar LED**: Acende e apaga o LED 5 vezes.
- **Desligar LED**: Garante que o LED fique apagado.

---

## 📈 Objetivo
Criar uma aplicação que demonstre comunicação entre um software em Python e um microcontrolador Arduino para realizar a tarefa de controle de LED, com uma interface amigável.

---

## 🚀 Tecnologias Utilizadas
- Python 3.x
- Arduino UNO
- IDE Arduino
- Bibliotecas Python: `pyserial`, `tkinter`, `python-dotenv`

---

## 🔧 Instalação e Execução

### 1. Clone o projeto e acesse a pasta
```bash
cd iot-arduino-python
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
# ou no Linux/macOS
python3 -m venv venv
```

### 3. Ative o ambiente virtual
```bash
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Configure a porta do Arduino no arquivo `.env`
Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
```
ARDUINO_PORT=COM3
```
Substitua `COM3` pela porta correspondente ao seu Arduino (ex: `/dev/ttyUSB0` no Linux).

### 6. Envie o código para o Arduino
Abra o arquivo `arduino/led_control.ino` na IDE Arduino e faça o upload para o dispositivo.

### 7. Execute o app
```bash
python app/main.py
```

---

## 📊 Estrutura do Projeto
```
iot-arduino-python/
├── arduino/
│   └── led_control.ino         # Código do Arduino
├── app/
│   └── main.py                 # Interface Python com tkinter
├── .env                        # Porta serial do Arduino
├── requirements.txt            # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```

---

## 👀 Resultado Esperado
Ao executar a aplicação:
- Um botão verde "Piscar LED" piscará o LED 5 vezes.
- Um botão vermelho "Desligar LED" manterá o LED apagado.

---

## 📄Montagem

Montagem com o LED no pino 13 com resistor de 220Ω:

```
+5V ----->|220R|----->| LED |-----> GND
```

---

## 👍 Contribuição
Este projeto foi desenvolvido como parte da disciplina **Engenharia de Software I** com foco em **Internet das Coisas**.

Trabalho da Equipe [João Barreto](https://github.com/jaobarreto), [Davi Mathais](https://github.com/cksalmeida) e [Luiz Guilherme](https://github.com/luizgfr).



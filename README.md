# ChatTTS: Modelo de Fala Generativa para Diálogos Diários  

O ChatTTS é um modelo de **conversão de texto em fala (TTS)** projetado especificamente para **cenários de diálogo**, oferecendo saídas de áudio naturais e expressivas.

---

## 🌍 **Idiomas Suportados**
- ✅ **Inglês**
- ✅ **Chinês**
- 🚧 **Mais idiomas em breve...**

---

## 📚 **Visão Geral do Modelo e Conjunto de Dados**

### ⚠️ Nota Importante  
O modelo disponibilizado é apenas para **uso acadêmico**.

### Principais Características:
- **Dados de Treinamento**: O modelo principal foi treinado com **mais de 100.000 horas (11 anos)** de dados de áudio em inglês e chinês.  
- **Versão Open Source**: Disponível no **[HuggingFace](https://huggingface.co/2Noise/ChatTTS)**, a versão pré-treinada contém 40.000 horas de dados (aproximadamente 4,5 anos) **sem ajuste fino supervisionado (SFT)**.

> **📝 Termos Importantes**  
> **Ajuste Fino Supervisionado (SFT)**: Processo de refinar um modelo pré-treinado utilizando dados rotulados para melhorar seu desempenho em tarefas específicas.  
> **Prosódia**: Refere-se à melodia e ao ritmo da fala, incluindo entonação, acentuação e timing, essenciais para uma saída natural e expressiva.

---

## 🚀 **Como Usar o ChatTTS**

### **Requisitos**
- **Versão do Python**: `>= 3.9 && < 3.13`  

### **Instalação**
1. Clone o repositório:  
  ```sh
  git clone https://github.com/LuccaRebelloToledo/chat-tts.git
  ```
2. Acesse o diretório do projeto:
  ```sh
  cd ./chat-tts
  ```
3. Instale as dependências:
  ```sh
  pip install -r requirements.txt
  ```
#### **Execute um Exemplo**
Use o comando abaixo para rodar um script de exemplo:
  ```sh
  python ./examples.py
  ```

---

### 🛠️ **Solução de Problemas**
#### **Problemas Comuns**
1. **Erro de Versão do Python:**
  Certifique-se de que está utilizando uma versão do Python entre 3.9 e 3.12.

2. **Dependências Não Instaladas:**
  Verifique se todas as dependências necessárias estão instaladas corretamente rodando:
  ```sh
  pip install -r requirements.txt
  ```
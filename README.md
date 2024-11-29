# ChatTTS
Um modelo de discurso generativo para diálogo diário.

### Sobre  
ChatTTS é um modelo de conversão de texto em fala projetado especificamente para cenários de diálogo.

### Idiomas suportados
- [x] Inglês
- [x] Chinês
- [ ] Em breve...

### Conjunto de dados e modelo
> [!Important]
> O modelo lançado é apenas para fins acadêmicos.

- O modelo principal é treinado com dados de áudio em inglês e chinês de mais de 100.000 horas. (11 anos)
- A versão de código aberto em **[HuggingFace](https://huggingface.co/2Noise/ChatTTS)** é um modelo pré-treinado de 40.000 horas sem SFT. (4,5 anos)

> [!Tip]
> Ajuste Fino Supervisionado(STF): É um processo onde um modelo pré-treinado é ajustado com dados rotulados adicionais para melhorar seu desempenho em uma tarefa específica.
> Prosódia: É a melodia e o ritmo da fala, envolvendo intonação, acentuação e ritmo para transmitir naturalidade e expressividade.

### Como utilizar

#### Requisitos
- Python >= 3.9 || < 3.13

#### Instalação
```sh
git clone https://github.com/LuccaRebelloToledo/chat-tts.git
cd ./chat-tts
pip install -r requirements.txt
```

#### Execução
```sh
python ./examples.py
```

### Solução de Problemas
- **Erro de versão do Python**: Certifique-se de que está usando uma versão do Python entre 3.9 e 3.12.
- **Dependências não instaladas**: Verifique se todas as dependências estão instaladas corretamente com `pip install -r requirements.txt`.
# Passando YouTube Shorts com comandos de voz

Esse simples código em Python passa vídeos do YouTube Shorts automaticamente, reconhecendo sua voz e faz as seguintes ações:

- Passa para o próximo vídeo
- Volta para o vídeo anterior
- Abre os comentários
- Dá o like no vídeo

**Atenção**: esse código foi feito utilizando como medidas das localizações do buttons o tamanho do meu celular, talvez, por seu celular ser diferente, os botões podem estar ligeiramente em diferentes posições.

## Como utilizar e como funciona

Baixe o código, execute no seu editor, e fique de olho no seu terminal

Vai aparecer um `listening...` e isso quer dizer que o código estará funcionando e que já está te escutando

**Para passar o vídeo:** basta dizer qualquer frase que contenha as palavras `vídeo`, `passar` ou `passar`

**Para voltar para o próximo vídeo:** basta dizer qualquer frase que contenha as palavras `anterior`, `voltar` ou `volta`

**Para acessar os comentários:** basta dizer qualquer frase que contenha a palavra 
`comentário`

**Para dar o like:** basta dizer qualquer frase que contenha a palavra `gostei`

## Como modificar os gatilhos para cada ação

Você pode modificar os gatilhos para cada ação modificando a seguinte parte do código

```python
if 'passa' in command or 'vídeo' in command or 'passar' in command:
 ## resto do código...
```

Basta substituir ou retirar as palavras `passa`, `vídeo` e `passar`. Assim os gatilhos para cada ação serão atividos pela palavras que você quiser

## Bibliotecas usadas

[Speech_Recognition v3.8.1](https://pypi.org/project/SpeechRecognition/3.8.1/) - Para reconhecimento de voz. A versão mais nova não estava reconhecendo as falas.

[Pure-Python-adb](https://pypi.org/project/pure-python-adb/) - Para reconhecer o aparelho conectado e realizar simulações de toques na tela do celular de maneira remota. Pode ser usado tanto no celular pessoal quanto no [emulador do Android Studio](https://developer.android.com/studio/run/emulator?hl=pt-br#runningapp)

## Se quiser mudar o idioma

Se quiser mudar o idioma, troque o `language='pt-BR'` para o [idioma que quiser](https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134). Segue o exemplo pra trocar pra inglês:

```python
command = listener.recognize_google(voice, language='en-US')
```
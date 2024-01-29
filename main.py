import speech_recognition as sr
from ppadb.client import Client

# Conecte-se ao dispositivo
adb = Client(host="127.0.0.1", port=5037)

devices = adb.devices()

for device in devices:
    print(device.serial)

if len(devices) == 0:
    print('no devices connected')
    quit()
device = devices[0]

listener = sr.Recognizer()

while True:
    def command_talk():
        try:
            with sr.Microphone() as source:
                print('listening...')
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language='pt-BR')
                if 'passa' in command or 'vídeo' in command or 'passar' in command:
                    print(command)
                    device.shell('input swipe 527 1630 527 1030 65')
                elif 'voltar' in command or 'volta' in command or 'anterior' in command:
                    print(command)
                    device.shell('input swipe 527 663 527 1663 55')
                elif 'comentários' in command:
                    print(command)
                    device.shell('input tap 991 1464')
                elif 'gostei' in command:
                    print(command)
                    device.shell('input tap 982 1079')
                else: print(command)

        except:
            pass
        
    command_talk()



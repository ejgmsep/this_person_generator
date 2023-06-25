import requests
import os
from pathlib import Path

def comprobate_path():
    if os.path.exists('Fotos'):
        download_loc = Path('./Fotos/')
    else:
        Path('Fotos').mkdir(exist_ok=True)
        download_loc = Path('./Fotos/')
        print(f'Carpeta {download_loc} creada')
  

def for_generate_face(number = 1):
    for i in range(number):
        response = requests.get('https://thispersondoesnotexist.com/')
        with open(rf'{os.getcwd()}/fotos/{i + 1}.jpg', 'wb') as f:
            f.write(response.content)
            print(f'Foto {i+1}/{number} descargada')


if __name__ == '__main__':

    comprobate_path()

    while True:
        response = requests.get('https://thispersondoesnotexist.com/')
        if response.status_code == 200:
            try:
                number = int(input('¿Cuantas fotos vas a descargar?: '))
                if number <= 1:
                    print('Solo acepto números mayores de 0')
                else:
                    for_generate_face(number)
                    print('Todas las fotos descargas')
                    input('ENTER PARA SALIR ')
                    break
            except ValueError:
                print('Solo acepto números')
        else:
            print(f'Error. Status error {response.status_code}')


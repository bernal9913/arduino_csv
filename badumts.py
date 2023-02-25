"""Para datalogge"""

import time
import serial
# si no jala serial, usar 'pip uninstall serial'
# posteriormente usar 'pip install pyserial'
# pd:  si sigue sin jalar, desinstalar pyserial y reinstalar
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv


def main():
    "Esta es el tiempo para que se pause la funcion y grafique."
    ts = 0.1
    tf = 10
    t = np.arange(0, tf + ts, ts)
    N = len(t)

    "El puerto se tiene que cambiar"
    port = 'COM5'
    baudRate = 9600
    sizeData = 8

    try:
        y = np.zeros((sizeData, N))

        arduino = serial.Serial(port, baudRate, sizeData)

        arduino.readSerialStart()

        for k in range(N):

            start_time = time.time()

            for n in range(sizeData):
                y[n.k] = arduino.rawData[n]

            print(f"Voltaje {y[0, k]}")
            print(f"Temperatura {y[1, k]}")

            elapsed_time = time.time() - start_time

            while elapsed_time < ts:
                elapsed_time = time.time() - start_time

        arduino.close()

    except Exception as e:
        print(e)

    try:
        plt_to_excel(t,y)

    except Exception as e:
        print(e)

def plt_to_excel(t, y):
    '''
    funcion para convertir el plt a un archivo csv
    :param t: tiempo o temperatura
    :param y: ni perra idea
    :return: 
    '''''
    plt.figure()
    plt.plot(t, y[0, :], label='Voltaje')
    plt.figure()
    plt.plot(t, y[1, :], label='Temperature')
    plt.legend(loc='upper left')
    plt.show()

    "Para guardar los datos en Excel"

    data = {'Voltaje': y[0, :],
            'Temperatura': y[1, :]}
    df = pd.DataFrame(data, columns=['Voltaje', 'Temperatura'])
    df.to_excel('DataLogger.csv')


if __name__ == '__main__':
    main()

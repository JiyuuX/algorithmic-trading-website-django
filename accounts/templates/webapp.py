

import websocket, json
import time
from decimal import *


SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@trade"



class Timer:
    _inittime = 0
    _waittime = 0
    _blocked = False

    @staticmethod
    def wait(seconds: int):
        Timer._blocked = True
        Timer._inittime = time.time()
        Timer._waittime = seconds

    @staticmethod
    def isfree() -> bool:
        if Timer._blocked:
            if time.time() - Timer._inittime > Timer._waittime:
                Timer.blocked = False
                return True
            else:
                return False

        else:
            return True

class Binance:
    anlik_deger = 0
    deger = 0

    alim = [1]
    satim = [3]

    degerler = {
        "alim": alim,
        "satim": satim,
    }

    deger2 = 0  # 2.Alımın tutuldugu degisken
    deger3 = 0  # 2.SAtımın tutuldugu degisken

    deger4 = 0  # 3.Alımın
    deger5 = 0  # 3.Satımın

    deger6 = 0  # 4.alımın
    deger7 = 0  # 4.SAtımın

    deger8 = 0  # 5.alımın
    deger9 = 0  # 5.satımın

    deger10 = 0  # 6.alımın
    deger11 = 0  # 6.satımın

    deger12 = 0  # 7.alımın
    deger13 = 0  # 7.satımın

    deger14 = 0  # 8.alımın
    deger15 = 0  # 8.satımın

    deger16 = 0  # 9.alımın
    deger17 = 0  # 9.satımın

    deger18 = 0  # 10.alımın
    deger19 = 0  # 10.satımın

    controlFlag = 0  # 1.Satımın olduğuna dair flag-1.alımın flagı yok zaten socket acıldıgı gibi ilk alımı yapıyor.
    controlFlag2 = 0  # 2.ALımın

    toplam = 0
    sinirOne = 2  # SATMA SARTI(ustten)
    sinirTwo = 2  # ALMA SARTI(asagıdan)

    @staticmethod
    def gercek_satma():
        print(f"Satim islemi gerceklesti, kar= {Binance.deger - Binance.anlik_deger}'dir")
        # TOPLAM KAR HESAPLAMA İCİN ALTTAKİ İKİ SATIR
        global toplam
        Binance.toplam += Decimal(Binance.deger) - Decimal(Binance.anlik_deger)

        Binance.anlik_deger = 999999999999999999999999999999  # Fonksiyonun tekrar calismasını engellemek icin koyduk bunu
        # Timer.wait()

        Binance.satim.append(Binance.deger)

    @staticmethod
    def gercek_satma2():
        print(f"Satim-2 islemi gerceklesti , kar= {Binance.deger3 - Binance.deger2} 'dir")
        # TOPLAM KAR HESAPLAMA İCİN ALTTAKİ İKİ SATIR
        global toplam
        Binance.toplam += Decimal(Binance.deger3) - Decimal(Binance.deger2)

        Binance.anlik_deger = 999999999999999999999999999998  # Fonksiyonun tekrar calismasını engellemek icin koyduk bunu
        global controlFlag2
        Binance.controlFlag2 = 0

        Binance.satim.append(Binance.deger3)

    @staticmethod
    def on_open(ws):
        print("Websocket baglantisi kuruldu...")
        #time.sleep(1)
        print("2 saniye sonra ilk alim gerceklestirilecek..")
        #time.sleep(2)

    @staticmethod
    def on_message(ws, message):
        if Timer.isfree():
            json_message = json.loads(message)
            value = float(json_message['p'])
            print(f"Veri alindi > {Binance.anlik_deger} > {value} > {json_message['p']}")


            # 1.ALIM
            if Binance.anlik_deger == 0:
                Binance.anlik_deger = value

                Binance.alim.append(Binance.anlik_deger)






            # 1.SATIM
            elif (Binance.anlik_deger) + (Binance.sinirOne) <= value:
                global deger
                Binance.deger = value
                Binance.gercek_satma()

                global controlFlag
                Binance.controlFlag = 1

            # 2-ALIM
            # print("Bİnance.deger'i 222 : " + str(Binance.deger))
            # print("control flag " + str(Binance.controlFlag))
            if (value <= ((Binance.deger) - (Binance.sinirTwo))) and (Binance.controlFlag == 1):
                print("ALim-2  yapildi")

                Binance.alim.append(value)

                global deger
                Binance.deger2 = value
                Binance.deger = 0
                global controlFlag2
                Binance.controlFlag2 = 1

            # 2-SATIM
            if (Binance.deger == 0) and (Binance.controlFlag2 == 1):
                if ((Binance.deger2) + (Binance.sinirOne)) <= value:
                    Binance.deger3 = value
                    Binance.gercek_satma2()

                    global controlFlag3
                    Binance.controlFlag3 = 1




    # ----------------------------------------------------------------

    def on_close(ws):
        print("Websocket baglantisi sonlandirildi...")
        print("-----------------------------------------------------")
        print("Toplam kazanc : " + str(Binance.toplam))
        print("-----------------------------------------------------")


if __name__ == '__main__':
    Timer.wait(2)
    ws = websocket.WebSocketApp(SOCKET, on_open=Binance.on_open, on_close=Binance.on_close,
                                on_message=Binance.on_message)

    ws.run_forever()

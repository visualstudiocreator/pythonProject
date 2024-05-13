import subprocess
import threading
import time

finished = False
content = "undef"
path = "/"


def doBack(text,file_path):
    with open(file_path, "w+") as f:
        f.write(text)
class alive(threading.Thread):
    def run(self):
        timer=0
        while(True):
            timer+=1
            time.sleep(1)
            if (timer>4):
                print("Время ожидания истекло")
                doBack(content,path)
                exit(-1)
            if (finished==True):
                break


def checkTask(file_path, SIGN ,values, res):
    alive().start()

    global path
    path = file_path

    with open(file_path, "r") as f:
        text = f.read()
        global content
        content = text

    with open(file_path, "a") as f:
        f.write("\n\n" + SIGN + "(" + values + ")")

    try:
        result = subprocess.check_output(["python", file_path], stderr=subprocess.STDOUT, text=True)
        if result[:-1] == res:
            print("Задача выполнена")
        else:
            print("Задача не выполнена")

        global finished
        finished = True
        doBack(text,file_path)

    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении файла:", e.output)
        doBack(text,file_path)

checkTask("test.py", "check","7,8","15")






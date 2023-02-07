import eel
eel.init('web')
eel.start('main.html',block=False)

print("This is now after start")

@eel.expose
def my_python_method(param1,param2):
    print(param1+param2)

eel.start('main.html',block=False)
eel.my_javascript_function("Hellow","Word")


while True:
    eel.sleep(10)

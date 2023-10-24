screen = int(input("Введите стоимость монитора:"))
print (" · Стоимость монитора:", screen)
system_unit = int(input("Введите стоимость системного блока:"))
print (" · Стоимость системного блока:", system_unit)
keyboard = int(input("Введите стоимость клавиатуры:"))
print (" · Стоимость клавиатуры:", keyboard)
computer_mouse = int(input("Введите стоимость компютерной мыши:"))
print (" · Стоимость компютерной мыши:", computer_mouse)

all = screen + system_unit + keyboard + computer_mouse
print (" · Общая стоимость: ", all)
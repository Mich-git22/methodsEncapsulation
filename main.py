from itertools import filterfalse

from classWindow import Window

ventana = Window()
ventana.setDimensions(500,500)
ventana.setTitulo("Mi primera App")
ventana.setResize(False)

# print(ventana.getDimensions())
# print(ventana.getResize())
# print(ventana.getTitulo())

ventana.crear_ventana()
def crearDiccionarios():
    d1 = {'x': "equis", 'y': "ye", 'd': "de"}
    d2 = dict(x="equis", y="ye", d="de")
    return d1, d2

def accesoValores(dic):
    print(dic['x'])
    print(dic.get('x'))
    print(dic.get('z'))

def modificarValores(dic):
    dic['x'] = "equis :O"
    print(dic['x'])

def agregarElemento(dic):
    dic['z'] = "zeta"
    print(dic['z'])

def eliminarElemento(dic):
    del dic['y']
    print(dic)

def eliminarConPop(dic):
    dic = {'x': "equis", 'y': "ye", 'd': "de"}
    eliminado = dic.pop('y')
    print(dic)
    print(eliminado)

def buscarClave(dic):
    print('x' in dic)

def mostrarClaves(dic):
    print(dic.keys())

def mostrarValores(dic):
    print(dic.values())

def diccionarioATuplas(dic):
    print(dic.items())

def vaciarDiccionario(dic):
    dic.clear()
    print(dic)

def actualizarDiccionario(dic):
    dic.update({'x': "Pitbull", 'y': "Yandell", 'd': "Ozuna"})
    print(dic)

def ejecutar():
    dic, dic2 = crearDiccionarios()
    accesoValores(dic)
    modificarValores(dic)
    agregarElemento(dic)
    eliminarElemento(dic)
    eliminarConPop(dic)
    buscarClave(dic)
    mostrarClaves(dic)
    mostrarValores(dic)
    diccionarioATuplas(dic)
    vaciarDiccionario(dic2)
    actualizarDiccionario(dic)

ejecutar()

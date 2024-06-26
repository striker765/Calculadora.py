valores = ''
def exibir_valor(campo, item):
    global valores
    valores += item
    campo.set(valores)

def resultado(campo):
    global valores
    try:
        resultado = eval(valores)
        campo.set(resultado)
        valores = str(resultado)
    except SyntaxError:
        campo.set("Erro de sintaxe")
        valores = ""

def limpar_campo(campo):
    global valores
    valores = ''
    campo.set('')
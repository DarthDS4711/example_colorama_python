#!/usr/bin/python
#santiago alatorre daniel
#moreno marquez hector adrian
#examen 01
import readchar
from colorama import init, Fore, Back, Cursor
from time import sleep
import os
init(autoreset=True)

# function for clean the window
def cls():
    os.system('clear')

# name of file
def name_enterprise():
    return "archivo.txt" 

#####################Archivos#########################
# block of functions to manage enterprise
def read_enterprise():
    name_company = ""
    file = open(name_enterprise(), mode="r", encoding="utf-8")
    for lines in file:
        if "!" in lines:
            name_company = lines[1:-1]
            break
    file.close()
    return name_company

#function to modify name company
def modify_enterprise(name_company):
    lines = []
    file = open(name_enterprise(), mode="r", encoding="utf-8")
    for line in file:
        if "!" in line:
            line = "!" + name_company + "\n"
        lines.append(line)
    file.close()
    file = open(name_enterprise(), mode="w", encoding="utf-8")
    file.writelines(lines)
    file.close()

# function for manage enterprise
def file_enterprise(option, name_company = ""):
    match option:
        case 0:#case of read
            return read_enterprise()
        case 1:#case of modify
            modify_enterprise(name_company)
            return ""
        case 2:# case of create
            modify_enterprise(name_company)
            return ""
        case 3:# case of erarse
            modify_enterprise(name_company)
            return ""
# ----------------------------- company ------------------------------------------


# main function for manage employees
def file_employee(option, name_employee = "", id_employee = 0):
    match option:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass

# -------------------------------- employees ------------------------------------------
# function for read products
def read_products():
    list_products = {}
    file = open(name_enterprise(), mode="r", encoding='utf-8')
    for line in file:
        if "#" in line:
            line = line[1:-1]
            line = line.split(";")
            list_products[line[0]] = [line[1], line[2], line[3]]
    file.close()
    return list_products

# function por modify product
def modify_product(name_product, id_product, price, ammount):
    file = open(name_enterprise(), mode="r", encoding="utf-8")
    second_file = open("temporaly.txt", mode="w", encoding="utf-8")
    for lines in file:
        if "#" in lines:
            line = lines[1:-1]
            line = line.split(";")
            if id_product == line[0]:
                lines = [id_product + ";" + name_product + ";" + price +";"+ ammount]
                lines = "".join(lines)
                lines = "#" + lines + "\n"
        second_file.write(lines)
    file.close()
    second_file.close()
    os.remove(name_enterprise())
    os.rename("temporaly.txt", name_enterprise())

# function for create a new product
def create_product(name_product, id_product, price, ammount):
    file = open(name_enterprise(), mode="r", encoding="utf-8")
    second_file = open("temporaly.txt", mode="w", encoding="utf-8")
    for line in file:
        if "%" in line:
            line = [id_product + ";" + name_product + ";" + price +";"+ ammount]
            line = "".join(line)
            line = "#" + line + "\n%\n"
        second_file.write(line)
    file.close()
    second_file.close()
    os.remove(name_enterprise())
    os.rename("temporaly.txt", name_enterprise())
 
        
def file_products(option, id_product = "", name_product = "", price = "0", ammount = "0"):
    match option:
        case 0:# read products
            return read_products()       
        case 1:# modify product
            modify_product(name_product, id_product, price, ammount)
        case 2:# create product

            pass
        case 3:
            pass


# ---------------------------------- products -------------------------------------------

def archivos(a,b,c,d,e,f):
    ar="archivo.txt"
    if(a==1):#Empleados
        if(b==0):#Busca Empleados
            empl={}
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "@" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        empl[linea[0]]=[linea[1]]
            archivo.close()
            if not empl:
                return 1;
            else:
                return empl;
        elif(b==1):#Modifica Empleados
            empleados=list()
            empleados2={}
            empleados3=""
            cont1=0
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "@" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        empleados2[linea[0]]=[linea[1]]
            archivo.close()
            for a in empleados2:
                if a==c:
                    empleados2[a]=[d]
                    cont1=1
            if cont1==0:
                return cont1;
            for a in empleados2:
                empl2=str(empleados2[a])
                linea=[str(a)+";"+str(empl2[2:-2])]
                linea="".join(linea)
                linea="@"+linea+"\n"
                empleados3+=linea
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "[Empleados]" in linea:
                        linea=linea+empleados3
                        empleados.append(linea)
                    elif "@" not in linea:
                        empleados.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(empleados)
            archivo.close()
        elif(b==2):#Crea Empleado
            empleados=list()
            empleados2={}
            empleados3=""
            cont1=0
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "@" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        empleados2[linea[0]]=[linea[1]]
            archivo.close()
            for a in empleados2:
                if a==c:
                    cont1=1
                    return cont1;
            if cont1==0:
                empleados2[c]=[d]
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for a in empleados2:
                    empl2=str(empleados2[a])
                    linea=[str(a)+";"+str(empl2[2:-2])]
                    linea="".join(linea)
                    linea="@"+linea+"\n"
                    empleados3+=linea
                for linea in archivo:
                    if "[Empleados]" in linea:
                        linea=linea+empleados3
                        empleados.append(linea)
                    elif "@" not in linea:
                        empleados.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(empleados)
            archivo.close()
            return cont1
        elif(b==3):#Borra Empleado
            empleados=list()
            empleados2={}
            empleados3=""
            cont1=0
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "@" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        for a in linea:
                            empleados2[linea[0]]=[linea[1]]
                archivo.close()
            if c in empleados2:
                del empleados2[c]
                cont1=1
            for a in empleados2:
                empl2=str(empleados2[a])
                linea=[str(a)+";"+str(empl2[2:-2])]
                linea="".join(linea)
                linea="@"+linea+"\n"
                empleados3+=linea
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "[Empleados]" in linea:
                        linea=linea+empleados3
                        empleados.append(linea)
                    elif "@" not in linea:
                        empleados.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(empleados)
            archivo.close()
            return cont1;
    elif(a==2):#Productos
        if(b==2):#Crea Productos
            productos=list()
            productos2={}
            productos3=""
            cont1=0
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "#" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        productos2[linea[0]]=[linea[1],linea[2],linea[3]]
            archivo.close()
            for a in productos2:
                if a==c:
                    cont1=1
                    return cont1;
            if cont1==0:
                productos2[c]=[d,e,f]
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for a in productos2:
                    pro2=str(productos2[a])
                    pro2=pro2[2:-2]
                    pro2=pro2.split("'")
                    pro2="".join(pro2)
                    pro2=pro2.split(", ")
                    linea=[str(a)+";"+str(pro2[0])+";"+str(pro2[1])+";"+str(pro2[2])]
                    linea="".join(linea)
                    linea="#"+linea+"\n"
                    productos3+=linea
                for linea in archivo:
                    if "[Productos]" in linea:
                        linea=linea+productos3
                        productos.append(linea)
                    elif "#" not in linea:
                        productos.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(productos)
            archivo.close()
            return cont1
        '''
        elif(a==3):#Venta Productos
            if(b==1):#Venta
                productos=list()
                productos2={}
                productos21={}
                productos3=""
                productos4=""
                cont1=0
                ven=""
            pv=str(d)
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "#" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        productos2[linea[0]]=[linea[1],linea[2],linea[3]]
            archivo.close()
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "$" in linea:
                        linea=linea[1:-1]
                        linea=linea.split(";")
                        productos21[linea[0]]=[linea[1],linea[2],linea[3]]
                print(productos21)
                for a in productos2:
                    if a==c:
                        prod2=productos2[a]
                        if int(prod2[1])>int(d):
                            e=int(prod2[1])-int(d)
                            productos2[a]=[prod2[0],str(e),prod2[2]]
                            cont1=1
                        else:
                            return cont1
                for a in productos2:
                    prod2=productos2[a]
                    prod2="#"+str(a)+";"+str(prod2[0])+";"+str(prod2[1])+";"+str(prod2[2])
                    productos3+=str(prod2)+"\n"
            archivo.close()
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "[Productos]" in linea:
                        linea+=productos3
                        productos.append(linea)
                    elif "#" not in linea:
                        productos.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(productos)
            archivo.close()
            productos=list()
            y=0
            for a in productos21:
                for b in productos2:
                    if b==a:
                        if a==c:
                            x=productos21[a]
                            z=productos2[a]
                            w=int(x[1])+int(pv)
                            productos21[a]=[z[0],w,z[2]]
                            print(productos21[a])
                            y=1
            if y==0:
                for a in productos2:
                    if a==c:
                        prod4=str(productos2[a])
                        prod4=prod4[2:-1]
                        prod4=prod4.split("'")
                        prod4="".join(prod4)
                        prod4=prod4.split(", ")
                        pv=int(d)
                        ven="$"+str(a)+";"+str(prod4[0])+";"+str(pv)+";"+str(prod4[2])
                for a in productos21:
                    prod6=productos21[a]
                    prod6="$"+str(a)+";"+str(prod6[0])+";"+str(prod6[1])+";"+str(prod6[2])
                    productos4+=prod6+"\n"
                productos4+=ven
            else:
                for a in productos21:
                    prod6=productos21[a]
                    prod6="$"+str(a)+";"+str(prod6[0])+";"+str(prod6[1])+";"+str(prod6[2])
                    productos4+=prod6+"\n"
            with open(ar,mode="r",encoding="utf-8") as archivo:
                for linea in archivo:
                    if "[Venta Productos]" in linea:
                        linea+=productos4
                        productos.append(linea)
                    if "$" not in linea:
                        productos.append(linea)
            archivo.close()
            with open(ar,mode="w",encoding="utf-8") as archivo:
                archivo.writelines(productos)
            archivo.close()
        '''
#sección de los titulos y descripciones################################################################################################################################
def tp(n):
    print(Cursor.POS(5,2)+"Modificar producto");
    print(Cursor.POS(5,3)+"Registrar producto");
    print(Cursor.POS(5,4)+"Borrar producto");
    print(Cursor.POS(5,5)+"Verificar almacén");
    print(Cursor.POS(5,6)+"Salir al menú principal");
    print(Cursor.POS(2,2)+"  ")
    print(Cursor.POS(2,3)+"  ")
    print(Cursor.POS(2,4)+"  ")
    print(Cursor.POS(2,5)+"  ")
    print(Cursor.POS(2,6)+"  ")
    if(n==2):
        print(Cursor.POS(5,2)+Back.YELLOW+"Modificar producto");
        print(Cursor.POS(2,2)+Fore.RED+"->")
    if(n==3):
        print(Cursor.POS(5,3)+Back.YELLOW+"Registrar Producto");
        print(Cursor.POS(2,3)+Fore.RED+"->")
    if(n==4):
        print(Cursor.POS(5,4)+Back.YELLOW+"Borrar producto");
        print(Cursor.POS(2,4)+Fore.RED+"->")
    if(n==5):
        print(Cursor.POS(5,5)+Back.YELLOW+"Verificar almacén");
        print(Cursor.POS(2,5)+Fore.RED+"->")
    if(n==6):
        print(Cursor.POS(5,6)+Back.YELLOW+"Salir al menú principal");
        print(Cursor.POS(2,6)+Fore.RED+"->")

def tm(n):
    name_company = file_enterprise(0)
    if name_company == "":
        print(Cursor.POS(44,5) + "Empresa no creada");
    else:
        print(Cursor.POS(44,5) + str(name_company));
    print(Cursor.POS(44,6)+"1.-Ventas");
    print(Cursor.POS(44,7)+"2.-Productos");
    print(Cursor.POS(44,8)+"3.-Empresa");
    print(Cursor.POS(44,9)+"4.-Registrar empleados");
    print(Cursor.POS(44,10)+"5.-Salir");
    print(Cursor.POS(40,6)+"  ");
    print(Cursor.POS(40,7)+"  ");
    print(Cursor.POS(40,8)+"  ");
    print(Cursor.POS(40,9)+"  ");
    print(Cursor.POS(40,10)+"  ");
    if(n<6):
        print(Cursor.POS(40,6)+Back.YELLOW+"->");
    if(n==6):
        print(Cursor.POS(44,6)+Back.YELLOW+"1.-Ventas");
        print(Cursor.POS(40,6)+Back.YELLOW+"->");
    if(n==7):
        print(Cursor.POS(44,7)+Back.YELLOW+"2.-Productos");
        print(Cursor.POS(40,7)+Back.YELLOW+"->");
    if(n==8):
        print(Cursor.POS(44,8)+Back.YELLOW+"3.-Empresa");
        print(Cursor.POS(40,8)+Back.YELLOW+"->");
    if(n==9):
        print(Cursor.POS(44,9)+Back.YELLOW+"4.-Registrar empleados");
        print(Cursor.POS(40,9)+Back.YELLOW+"->");
    if(n==10):
        print(Cursor.POS(44,10)+Back.YELLOW+"5.-Salir");
        print(Cursor.POS(40,n)+Back.YELLOW+"->");
def te(n):
    print(Cursor.POS(9,4)+"Registrar empleados");
    print(Cursor.POS(9,5)+"Modificar empleados");
    print(Cursor.POS(9,6)+"Eliminar empleados");
    print(Cursor.POS(9,7)+"Mostrar empleados");
    print(Cursor.POS(9,8)+"Salir");
    print(Cursor.POS(6,4)+"  ");
    print(Cursor.POS(6,5)+"  ");
    print(Cursor.POS(6,6)+"  ");
    print(Cursor.POS(6,7)+"  ");
    print(Cursor.POS(6,8)+"  ");
    if(n==4):
        print(Cursor.POS(9,4)+Back.YELLOW+"Registrar empleados");
        print(Cursor.POS(6,4)+Fore.RED+"->")
    if(n==5):
        print(Cursor.POS(9,5)+Back.YELLOW+"Modificar empleados");
        print(Cursor.POS(6,5)+Fore.RED+"->")
    if(n==6):
        print(Cursor.POS(9,6)+Back.YELLOW+"Eliminar empleados");
        print(Cursor.POS(6,6)+Fore.RED+"->")
    if(n==7):
        print(Cursor.POS(9,7)+Back.YELLOW+"Mostrar empleados");
        print(Cursor.POS(6,7)+Fore.RED+"->")
    if(n==8):
        print(Cursor.POS(9,8)+Back.YELLOW+"Salir");
        print(Cursor.POS(6,8)+Fore.RED+"->")
######################################################################################################################################################################
def ventana(a,b,c,d,e):
    col=e
    colores=["YELLOW","BLUE","RED","GREEN","MAGENTA","CYAN"];
    Color=getattr(Fore, colores[col])
    for i in range(a,b):
        print(Cursor.POS(i,c)+Color+"▀");
        print(Cursor.POS(i,d)+Color+"▀");
    for x in range(c,d):
        print(Cursor.POS(a,x)+Color+"█");
        print(Cursor.POS(b-1,x)+Color+"█")

def ventas():
    cls()
    carrito={}
    list_products = {}
    empleados = archivos(1,0,0,0,0,0)
    ventana(40,80,4,10,3)
    while True:
        try:
            cod = int(input(Cursor.POS(41,5)+Fore.RED+"Ingresa tu código de empleado: "))
            break
        except:
            print(Cursor.POS(41,6)+"Ingresaste un dato inválido")
    cls()
    ventana(1,50,2,7,4)
    print(Cursor.POS(2,3)+Fore.RED+"Estimado empleado por favor")
    print(Cursor.POS(2,4)+Fore.BLUE+"Revise que la cantidad en caja")
    print(Cursor.POS(2,5)+Fore.BLUE+"Sean $300 gracias")
    sleep(3)
    list_products = file_products(0)
    cls()
    while True:
        f=1
        for x in list_products:
            f+=1
            print(Cursor.POS(72,f) + "" , x , ":" , list_products[x])
        ventana(71,130,1,f+1,5)
        ventana(1,70,1,10,0)
        print(Cursor.POS(2,2) + "                                                                   ")
        id_product = str(input(Cursor.POS(2,2)+Fore.GREEN+"Ingrese el código del producto: "))
        while id_product.isdigit() == False:
            id_product = str(input(Cursor.POS(2,2) + Fore.GREEN + "Ingrese el código del producto nuevamente: "))
        id_product = int(id_product)
        if id_product == 0:
            cls()
            menu()
            break
        if list_products.get(str(id_product)) != None:
            while(1):
                try:
                    can = int(input(Cursor.POS(2,3)+"Ingrese la cantida que desee llevar: "))
                    while(1):
                        w = list_products[str(id_product)]
                        if can == None:
                            print(Cursor.POS(2,3)+"                                                                   ")
                            can=int(input(Cursor.POS(2,3)+"La cantidad no puede ser 0 intente de nuevo: "))
                        elif can>int(w[1]):
                            print(Cursor.POS(2,3)+"                                                                   ")
                            can=int(input(Cursor.POS(2,4)+"Ingreso una cantidad muy grande intente de nuevo: "))
                        else:
                            if carrito.get(str(ven))!=None:
                                k=carrito[str(ven)]
                                carrito[str(ven)]=[w[0],k[1]+can,int(w[2])]
                            else:
                                carrito[str(ven)]=[w[0],can,int(w[2])]
                            s=int(w[1])-can
                            list_products[str(id_product)] = [w[0],str(s),str(w[2])]
                            f=1
                            for x in list_products:
                                f+=1
                                print(Cursor.POS(72,f)+"",x,":", list_products[x])
                            print(Cursor.POS(2,5)+"Producto agregado al carrito")
                            sleep(1)
                            break;
                    break;
                except:
                    print(Cursor.POS(2,9)+Fore.RED+"Dato invalido")
            while(1):
                cls()
                ventana(1,70,1,10,0)
                cot=str(input(Cursor.POS(2,2)+"Desea continuar, eliminar o finalizar? (c/E/f): "))
                if cot=="c" or cot=="C":
                    break;
                elif cot=="e" or cot=="E":
                    cls()
                    ventana(1,70,1,10,0)
                    f=1
                    for x in carrito:
                        f+=1
                        print(Cursor.POS(72,f)+"",x,":", carrito[x])
                        ventana(71,130,1,f+1,5)
                    while(1):
                        try:
                            cod=int(input(Cursor.POS(2,2)+"Ingrese el codigo de producto a eliminar: "))
                            if carrito.get(str(cod))==None:
                                print(Cursor.POS(2,9)+Fore.RED+"Dato invalido intente de nuevo")
                            elif carrito.get(str(cod))!=None:
                                while(1):
                                    cel=str(input(Cursor.POS(2,3)+"Desea continuar con la eliminacion? (s/N): "))
                                    print(cel)
                                    if cel=="s" or cel=="S":
                                        w=carrito[str(cod)]
                                        y = list_products[str(cod)]
                                        s = int(y[1])+int(w[1])
                                        list_products[str(cod)] = [w[0],str(s),str(w[2])]
                                        del carrito[str(cod)]
                                        print(Cursor.POS(2,5)+"Producto eliminado")
                                        sleep(1)
                                        break;
                                    elif cel=="n" or cel=="N":
                                        break
                        except:
                            print(Cursor.POS(2,9)+Fore.RED+"Dato invalido intente de nuevo")
                elif cot=="f" or cot=="F":
                    for a in carrito:
                        carr=carrito[a]
                        archivos(3,1,str(a),int(carr[1]),0,0)
                        menu()
                    break;
            
                else:
                    print(Cursor.POS(2,9)+Fore.RED+"Dato invalido intente de nuevo")    
    

#Funciones de la sección de productos/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def return_components_of_product():
    cls()
    ventana(1,50,1,5,1)
    ammount = 0
    price = 0
    name_product = str(input("Ingresa el nombre del producto: "))
    while True:
        try:
            ammount = int(input("Ingresa la cantidad del producto: "))
            break
        except:
            print("Dato invalido intente de nuevo")
    while True:
        try:
            price = int(input("Ingresa el precio del producto: "))
            break
        except:
            print("Dato invalido intente de nuevo")
        break
    return ammount, price, name_product

def modify_actual_product(list_products):
    id_product = ""
    cls()
    ventana(1,50,1,5,1)
    try:
        id_product = str(input(Cursor.POS(2,2) + "Ingresa el código del producto: "))
        if id_product.isdigit() == False:
            modify_actual_product(list_products)
    except:
        modify_actual_product(list_products)
    if list_products.get(str(id_product)) == None:
        modify_actual_product(list_products)
    ammount, price, name_product = return_components_of_product()
    try:
        option = str(input("Desea modificar? (s/N): "))
        if option == "s" or option == "S":
            file_products(1, id_product, name_product, str(price), str(ammount))  
            productos()
    except:
        print("Dato invalido")
def p3(prod):
    x=0;
    while(x==0):
        for i in range(0,255):
            try:
                pr=int(input("Ingrese el codigo del producto a eliminar: "));
                break;
            except:
                print("Dato invalido");
        y=0
        while(1):
            g=str(input("Esta seguro de querer continuar?: "))
            if(g=="s" or g=="S"):
                y=1
                break;
            elif(g=="n" or g=="N"):
                break;
        if(y==1):
            print(prod.get(str(pr)))
            if(prod.get(str(pr))==None):
                print("El producto no existe");
            if(prod.get(str(pr))!=None):
                archivos(2,3,str(pr),0,0,0)
                x=1;
                sleep(5);
                cls()
                productos()


def create_new_product():
    option = str(input(Cursor.POS(1,5)+"Los datos son correctos? (s/N): "));
    if option == "s" or option == "S":
        pass
    elif option == "n" or option == "N":
        pass
    else:
        print("Ingreso un dato invalido intente de nuevo")


def p4(prod):
    for x in prod:
        print(x, " :",prod[x])
    sleep(5)
    productos()

# main function for enterprise
def empresa():
    cls()
    name_company = file_enterprise(0)
    if name_company == "":
        while True:
                ventana(1,50,1,5,2)
                name_of_company = str(input(Cursor.POS(2,2)+"Ingresa el nombre de tu empresa: "))
                if name_of_company != None:
                    file_enterprise(1, name_of_company)
                    break
                else:
                    print(Cursor.POS(2,3)+"Dato invalido intente de nuevo")
    else :
        while True:
            ventana(1,86,1,5,2)
            option = str(input(Cursor.POS(2,2) + "El nombre de empresa ya esta definido desea cambiarlo,borrarlo o salir? (c/B/s): "));
            cls()
            if option == "c":
                while True:
                    ventana(1,50,1,5,2)
                    name_of_company = str(input(Cursor.POS(2,2)+"Ingresa el nombre de tu empresa: "));
                    if name_of_company != None:
                        file_enterprise(2, name_of_company)
                        print("Nombre modificado con exito")
                        sleep(5)
                        menu()
                        break
                    else:
                        print(Cursor.POS(2,3)+"Dato invalido intente de nuevo")
            elif option == "b" or option =="B":
                file_enterprise(3)
                print("Empre borrada con exito")
                sleep(5)
                menu()
                break
            elif option == "s" or option == "S":
                menu()
                break
            else:
                print(Cursor.POS(2,3)+"Dato invalido intente de nuevo")        
    menu()

def productos():
    cls()
    ventana(1,40,1,7,3);
    n=2;
    tp(n)
    while True:
        list_products = file_products(0)
        key = readchar.readkey()
        if ord(key) == 115:
            n += 1
            if n > 6:
                n = 2
        if ord(key) == 119:
            n -= 1
            if n < 2:
                n = 6
        tp(n)
        match ord(key):
            case 13:
                match n:
                    case 2:
                        cls()
                        modify_actual_product(list_products)
                    case 3:
                        cls()
                        p2()
                    case 4:
                        cls()
                        p3(list_products)
                    case 5:
                        cls()
                        p4(list_products)
                    case 6:
                        cls()
                        menu()
                        break

#Sección de funciones de los empleados, registro, modificación o eliminar su código
def em0(eg):
    for x in eg:
        print(x, " :",eg[x])
    sleep(5)
    productos()

def em1(eg):
    x=0;
    while(x==0):
        while(1):
            for i in range(0,255):
                try:
                    cod=int(input("Ingresa el código del empleado: "));
                    if cod==-1:
                        empleados()
                    cls()
                    break;
                except:
                    print("Dato ingredado no valido");
            for i in range(0,255):
                try:
                    emp=str(input("Ingresa el nombre del empleado"));
                    cls()
                    break;
                except:
                    print("Dato ingresado no valido");
            cls()
            print(str(cod)+"\n"+emp)
            while(1):
                g=str(input("Los datos son correctos? (s/N): "))
                if g=="S" or g=="s":
                    le=archivos(1,2,str(cod),emp,0,0)
                    if le==1:
                        print("El codigo ya existe intente de nuevo");
                        z=0;
                    else:
                        print("Empleado registrado")
                        z=1;
                    break;
                elif g=="N" or g=="n":
                    print("Ingrese los datos de nuevo")
                    z=0;
            if z==1:
                break;
        for i in range(0,255):
            try:
                ex=str(input("Desea continuar: "));
                if(ex=="s" or ex=="S"):
                    eg=archivos(1,0,0,0,0,0)
                    break;
                if(ex=="n" or ex=="N"):
                    x=1;
                    print(eg)
                    empleados()
                    break
            except:
                print("Dato invalido");

def em2(eg):
    x=0;
    while(x==0):
        while(1):
            for i in range(0,255):
                try:
                    cod=int(input("Ingresa el código del empleado: "));
                    if cod==-1:
                        empleados()
                    cls()
                    break;
                except:
                    print("Dato ingredado no valido");
            for i in range(0,255):
                try:
                    emp=str(input("Ingresa el nombre del empleado"));
                    cls()
                    break;
                except:
                    print("Dato ingresado no valido");
            cls()
            print(str(cod)+"\n"+emp)
            while(1):
                g=str(input("Los datos son correctos? (s/N): "))
                if g=="S" or g=="s":
                    le=archivos(1,1,str(cod),emp,0,0)
                    if le==1:
                        print("El codigo ya existe intente de nuevo");
                        z=0;
                    else:
                        print("Empleado modificado")
                        z=1;
                    break;
                elif g=="N" or g=="n":
                    print("Ingrese los datos de nuevo")
                    z=0;
            if z==1:
                break;
        for i in range(0,255):
            try:
                ex=str(input("Desea continuar: "));
                if(ex=="s" or ex=="S"):
                    eg=archivos(1,0,0,0,0,0)
                    break;
                if(ex=="n" or ex=="N"):
                    x=1;
                    print(eg)
                    empleados()
                    break
            except:
                print("Dato invalido"); 


def em3(eg):
    x=0;
    while(x==0):
        for i in range(0,9999):
            try:
                while(1):
                    em=int(input("Ingresa el empleado a eliminar: "));
                    if em==-1:
                        empleados()
                    if(eg.get(str(em))==None):
                        cls()
                        print("El empleado no existe intenta de nuevo")
                    if(eg.get(str(em))!=None):
                        ax=archivos(1,3,str(em),0,0,0)
                        if ax==0:
                            print("El empleado no existe intente de nuevo")
                        else:
                            print("Empleado borrado")
                            sleep(5)
                            cls()
                            break;
                break;
            except:
                print("Ingresaste un dato inválido")
        for i in range(0,255):
            try:
                ex=str(input("Desea continuar (s/N): "));
                if(ex=="s" or ex=="S"):
                    eg=archivos(1,0,0,0,0,0)
                    x=0;
                    break;
                if(ex=="n" or ex=="N"):
                    empleados()
                    break;
                else:
                    print("Dato invalido")
            except:
                print("Dato invalido")

def empleados():
    cls()
    n=4
    ventana(5,40,3,9,4);
    te(n)
    for i in range(0,999999):
        eg=archivos(1,0,0,0,0,0)
        if(eg==1):
            print(Cursor.POS(45,5)+Fore.WHITE+"No hay empleados aun")
        elif(eg!=1):
            print(Cursor.POS(61,5)+"    ")
            print(Cursor.POS(45,5)+Fore.WHITE+"Ya hay empleados")
        z=msvcrt.getch()
        if(ord(z)==80):
            n+=1
            if(n>7):
                n=4;
            te(n)
        elif(ord(z)==72):
            n-=1
            if(n<4):
                n=7;
            te(n)
        if(ord(z)== 13 and n==4):
            cls()
            em1(eg)
        elif(ord(z)== 13 and n==5):
            cls()
            em2(eg)
        elif(ord(z)== 13 and n==6):
            cls()
            em3(eg)
        elif(ord(z)== 13 and n==7):
            cls()
            em0(eg)
        elif(ord(z)== 13 and n==8):
            cls()
            menu()


def menu():
    n=6;
    cls()
    ventana(39,77,4,11,2)
    tm(n)
    while(True):
        print(Cursor.POS(40,n) + Back.YELLOW + "->")
        key = readchar.readkey()
        if ord(key) == 115:
            n+=1
            if n > 10:
                n = 6;
                tm(n)
            print(Cursor.POS(40,n) + Back.YELLOW + "->")
            tm(n)
        elif ord(key) == 119:
            n-=1
            if n < 6:
                n = 10
                tm(n)
            print(Cursor.POS(40,n) + Back.YELLOW + "->")
            tm(n)
        if ord(key)==13 and n==6:
            cls()
            ventas()
        elif ord(key) == 13 and n == 7:
            cls()
            productos()
        elif ord(key) == 13 and n == 8:
            cls()
            empresa()
        elif ord(key) == 13 and n == 9:
            cls()
            empleados()
        elif ord(key) == 13 and n == 10:
            break

# start of program excecution 
if __name__ == "__main__":
    cls()
    ventas()


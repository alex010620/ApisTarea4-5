import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from datetime import datetime
import pymysql
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {'Sistema': 'Tarea4-5DB-YAMC'}

@app.post("/api/RegistroCuentaAhorro/{NoCuenta}/{Balance}")
def RegistroAdmin(NoCuenta: str,Balance:str):
    try:
        cor = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoCuenta FROM CuentasAhorro WHERE NoCuenta = '"+NoCuenta+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
        if NoCuenta == cor:
            return  {"ok":False}
        else:
            datos = (NoCuenta,Balance)
            sql='''INSERT INTO CuentasAhorro(NoCuenta,Balance) VALUES(?,?)'''
            cursor.execute(sql,datos)
            conexion.commit()
            return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.get("/api/RetiroCuentaAhorro/{NoCuenta}")
def RetiroCuentaAhorro(NoCuenta: str):
    try:
        cor = ""
        bal = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoCuenta, Balance FROM CuentasAhorro WHERE NoCuenta = '"+NoCuenta+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
            bal=i[1]
        if NoCuenta == cor:
            return  {"ok":True, "Cuenta":cor, "Balance":bal}
        else:
            return  {"ok":False}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/ActualizarBalanceCuentaAhorro/{NoCuenta}/{Balance}")
def ActualizarBalanceCuentaAhorro(NoCuenta: str, Balance: str):
    try:
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE CuentasAhorro SET Balance = '"+Balance+"' WHERE NoCuenta = '"+NoCuenta+"'")
        conexion.commit()
        return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/RegistroPrestamos/{numero}/{valor}/{taza}")
def RegistroPrestamos(numero: str,valor:str,taza:str):
    try:
        cor = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT numero FROM Prestamos WHERE numero = '"+numero+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
        if numero == cor:
            return  {"ok":False}
        else:
            datos = (numero,valor,taza)
            sql='''INSERT INTO Prestamos(numero,valor,taza) VALUES(?,?,?)'''
            cursor.execute(sql,datos)
            conexion.commit()
            return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.get("/api/SeleccionarPrestamo/{numero}")
def SeleccionarPrestamo(numero: str):
    try:
        cor = ""
        bal = ""
        taz=""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT numero,valor,taza FROM Prestamos WHERE numero = '"+numero+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
            bal=i[1]
            taz=i[2]
        if numero == cor:
            return  {"ok":True, "numero":cor, "Balance":bal, "taza":taz}
        else:
            return  {"ok":False}
    except TypeError:
        return "Error al conectar a la base de datos."
    
@app.post("/api/ActualizarPrestamo/{numero}/{Balance}")
def ActualizarPrestamo(numero: str, Balance: str):
    try:
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE Prestamos SET valor = '"+Balance+"' WHERE numero = '"+numero+"'")
        conexion.commit()
        return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/RegistroTajetas/{NoTarjeta}/{Limite}/{BalancePendiente}")
def RegistroTajetas(NoTarjeta: str,Limite:str,BalancePendiente:str):
    try:
        cor = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoTarjeta FROM Tarjetas WHERE NoTarjeta = '"+NoTarjeta+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
        if NoTarjeta == cor:
            return  {"ok":False}
        else:
            datos = (NoTarjeta,Limite,BalancePendiente)
            sql='''INSERT INTO Tarjetas(NoTarjeta,Limitte,BalancePendiente) VALUES(?,?,?)'''
            cursor.execute(sql,datos)
            conexion.commit()
            return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/ActualizarLimite/{numero}/{Balance}")
def ActualizarLimite(numero: str, Balance: str):
    try:
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE Tarjetas SET Limitte = '"+Balance+"' WHERE NoTarjeta = '"+numero+"'")
        conexion.commit()
        return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/ActualizarBalancePendienteTarjeta/{numero}/{Balance}")
def ActualizarBalancePendienteTarjeta(numero: str, Balance: str):
    try:
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE Tarjetas SET BalancePendiente = '"+Balance+"' WHERE NoTarjeta = '"+numero+"'")
        conexion.commit()
        return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.get("/api/SeleccionarTarjeta/{numero}")
def SeleccionarTarjeta(numero: str):
    try:
        cor = ""
        bal = ""
        taz=""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoTarjeta,Limitte,BalancePendiente FROM Tarjetas WHERE NoTarjeta = '"+numero+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
            bal=i[1]
            taz=i[2]
        if numero == cor:
            return  {"ok":True, "numero":cor, "Balance":int(bal), "pendiente":int(taz)}
        else:
            return  {"ok":False}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.post("/api/RegistroCertificado/{NoCertificado}/{Balance}/{Tiempo}/{TipoTiempo}")
def RegistroCertificado(NoCertificado: str,Balance:str,Tiempo:str,TipoTiempo:str):
    try:
        cor = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoCertificado FROM Certificados WHERE NoCertificado = '"+NoCertificado+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
        if NoCertificado == cor:
            return  {"ok":False}
        else:
            datos = (NoCertificado,Balance,Tiempo,TipoTiempo)
            sql='''INSERT INTO Certificados(NoCertificado,Balance,Tiempo,TipoTiempo) VALUES(?,?,?,?)'''
            cursor.execute(sql,datos)
            conexion.commit()
            return  {"ok":True}
    except TypeError:
        return "Error al conectar a la base de datos."

@app.get("/api/SeleccionarInteres/{numero}")
def SeleccionarInteres(numero: str):
    try:
        cor = ""
        bal = ""
        conexion = sqlite3.connect("tarea4-5db.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT NoCertificado, Balance FROM Certificados WHERE NoCertificado = '"+numero+"'")
        contenido = cursor.fetchall()
        for i in contenido:
            cor = i[0]
            bal = i[1]
        if numero == cor:
            return  {"ok":True, "numero":bal}
        else:
            return  {"ok":False}
    except TypeError:
        return "Error al conectar a la base de datos."
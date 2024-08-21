from sqlalchemy import text
from sqlalchemy.orm import Session
from decimal import Decimal
from service.utils import generate_no_rekening
from typing import Optional


#Select NIK or NO_HP is exsist
def nik_or_hp_exist(db: Session, nik: str, no_hp: str)-> bool:
    statement = text("""
        SELECT CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END
        FROM data_nasabah
        WHERE nik = :nik OR no_hp = :no_hp
    """)
    result = db.execute(statement,{
        'nik': nik,
        'no_hp': no_hp
    })
    count = result.scalar()
    return count == 1

#CekNorek Exist
def is_no_rekening_exist(db: Session, no_rekening: str) -> bool:
    statement = text("SELECT COUNT(*) FROM data_nasabah WHERE no_rekening = :no_rekening")
    result = db.execute(statement, {'no_rekening': no_rekening})
    return result.scalar() > 0

#Insert by Nik or No_HP
def insert_account_nasabah(db:Session, nama: str, nik: str, no_hp: str, no_rekening: str, saldo: Decimal):
    
    statement = text("""
        INSERT INTO data_nasabah (nama, nik, no_hp, no_rekening, saldo, created_at)
        VALUES (:nama, :nik, :no_hp, :no_rekening, :saldo, NOW())
        RETURNING no_rekening
    """)
    result = db.execute(statement,{
        'nama': nama,
        'nik': nik,
        'no_hp': no_hp,
        'no_rekening': no_rekening,
        'saldo': saldo
    })
    db.commit()
    return result.scalar() 

#Query Select All Data Nasabah where Rekening
def FindRekening(db: Session, no_rekening: str):
    statement = text("""
        SELECT * FROM data_nasabah WHERE (no_rekening = :no_rekening)
    """)
    result = db.execute(statement, {
        'no_rekening' : no_rekening
    })
    return result.fetchall()

#Query Update Tabungan 
def UpdateTabunganNasabah(db:Session, saldo: Decimal, no_rekening: str):
    statement = text("""
        UPDATE data_nasabah 
        SET saldo = :saldo, modified_at = NOW() 
        WHERE no_rekening = :no_rekening
    """)
    db.execute(statement, {
        'saldo' : saldo,
        'no_rekening' : no_rekening
    })
    db.commit()

#get Saldo
def GetSaldoByRekening(db: Session, no_rekening: str) -> Optional[Decimal]:
    query = text("SELECT saldo FROM data_nasabah WHERE no_rekening = :no_rekening")
    result = db.execute(query, {'no_rekening': no_rekening}).fetchone()
    if result:
        return Decimal(result['saldo'])
    return None

def generate_unique_no_rekening(db) -> str:
    while True:
        # Generate no_rekening
        no_rekening = generate_no_rekening()
        # Cek apakah no_rekening sudah ada
        if not is_no_rekening_exist(db, no_rekening):
            return no_rekening

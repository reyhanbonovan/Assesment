from datetime import datetime
from decimal import Decimal
from models.databaseModels import nik_or_hp_exist, insert_account_nasabah, generate_unique_no_rekening
from helpers.config import Config as config
from exception.appException import AppException
from schemas.svcAccountSchemas import ServiceRegisResponse
from loguru import logger as log
import json

def RegistrasiNasabahAcc(req, db):
    loggerId = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.info(f"{loggerId} - Start to processing Registrasi Nasabah. Request: \n{json.dumps(dict(req))}")
    #Request Mapping
    nama = req.nama
    nik = req.nik
    no_hp = req.no_hp
    #Cek 
    isExist = nik_or_hp_exist(db, nik, no_hp)
    if (isExist == True):
        log.warning(f"{loggerId} - NIK atau No HP sudah digunakan")
        raise AppException(config.param_error['nik_hp_exist'][0], config.param_error['nik_hp_exist'][1])
    
    saldo = Decimal('0.00')  # Set default saldo
    no_rekening = generate_unique_no_rekening(db)

    no_rekening = insert_account_nasabah(db, nama, nik, no_hp, no_rekening, saldo)
    log.info(f"{loggerId} - Nasabah berhasil didaftarkan dengan no_rekening: {no_rekening}")
    return ServiceRegisResponse(code=200, no_rekening=no_rekening)

from datetime import datetime
from decimal import Decimal
from models.databaseModels import FindRekening, UpdateTabunganNasabah
from schemas.svcAccountSchemas import ServiceTabungResponse
from helpers.config import Config as config
from exception.appException import AppException
from loguru import logger as log
import json

def TabungSaldoAcc(req, db):
    loggerId = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.info(f"{loggerId} - Start to processing menambahkan saldo. Request: \n{json.dumps(dict(req))}")
    #Request Mapping
    no_rekening = req.no_rekening
    nominal = Decimal(req.nominal)
    #Cek Rekening Exist or No
    listRekening = FindRekening(db, no_rekening)
    if not listRekening:
        log.warning(f"{loggerId} - No Rekening tidak ditemukan")
        raise AppException(config.param_error['rekening_no_exist'][0], config.param_error['rekening_no_exist'][1])
    #Logic Tambah Saldo
    rekening = listRekening[0]
    saldoTemp = 0 if rekening['saldo'] in [None, ''] else rekening['saldo'] 
    saldo = saldoTemp + nominal
    #Save saldo yang telah di tambahkan ke DB
    UpdateTabunganNasabah(db, saldo, no_rekening)
    log.info(f"{loggerId} - Nasabah berhasil menambahkan saldo. saldo terakhir: {saldo}")
    #Tampilan Result
    return ServiceTabungResponse(code=200, no_rekening=no_rekening, saldo=str(saldo))
from datetime import datetime
from decimal import Decimal
from models.databaseModels import GetSaldoByRekening
from schemas.svcAccountSchemas import SaldoResponse
from helpers.config import Config as config
from exception.appException import AppException
from loguru import logger as log
import json

def GetSaldoAcc(db, no_rekening: str) -> SaldoResponse:
    loggerId = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.info(f"{loggerId} - Start to processing menampilkan saldo. Request: \n{json.dumps({'no_rekening': no_rekening})}")
    saldo = GetSaldoByRekening(db, no_rekening)
    if saldo is None:
        raise AppException(config.param_error['rekening_no_exist'][0], config.param_error['rekening_no_exist'][1])
    log.info(f"{loggerId} - Menampilkan saldo. Saldo: \n{json.dumps({'saldo': float(saldo)})}")
    return SaldoResponse(saldo=str(saldo))
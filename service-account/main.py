from fastapi import FastAPI, Depends, Path
import uvicorn
from sqlalchemy.orm import Session
from typing import Union

from exception.globalException import global_exception
from schemas.svcAccountSchemas import ReqRegisNasabah, ReqTabungSaldo, ReqTarikSaldo, ServiceRegisResponse, ServiceTabungResponse, SaldoResponse, ServiceTarikResponse, ErrorResponse
from service.registrasiNasabah import RegistrasiNasabahAcc
from service.tabungSaldo import TabungSaldoAcc
from service.tarikSaldo import TarikSaldoAcc
from service.getSaldo import GetSaldoAcc
from helpers.config import Config as config
from models.databaseConnection import get_db



def create_app() -> FastAPI:
    app = FastAPI(title='MS Service Account', debug=True) # Dev Settings
    return app

app = create_app()
global_exception(app)

@app.post('/daftar', response_model=Union[ServiceRegisResponse, ErrorResponse])
def RegisterAccountNasabah(req:ReqRegisNasabah, db: Session = Depends(get_db)):
    return RegistrasiNasabahAcc(req, db)

@app.post('/tabung', response_model=Union[ServiceTabungResponse, ErrorResponse])
def TabunganNasabah(req:ReqTabungSaldo, db: Session = Depends(get_db)):
    return TabungSaldoAcc(req, db)

@app.post('/tarik', response_model=Union[ServiceTarikResponse, ErrorResponse])
def TarikSaldo(req:ReqTarikSaldo, db: Session = Depends(get_db)):
    return TarikSaldoAcc(req, db)

@app.get('/saldo/{no_rekening}', response_model=Union[SaldoResponse, ErrorResponse])
def get_saldo(no_rekening: str = Path(..., description="Nomor rekening nasabah"), db: Session = Depends(get_db)):
    return GetSaldoAcc(db, no_rekening)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host=config.app_host, port=config.app_port, workers=config.app_worker)



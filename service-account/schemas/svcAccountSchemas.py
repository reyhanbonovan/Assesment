from pydantic import BaseModel
from typing import Optional

#Request Schemas
class ReqRegisNasabah(BaseModel):
    nama: str
    nik: str
    no_hp: str

class ReqTabungSaldo(BaseModel):
    no_rekening: str
    nominal: str

class ReqTarikSaldo(BaseModel):
    no_rekening: str
    nominal: str

#Response Schemas
class ServiceRegisResponse(BaseModel):
    code: int
    no_rekening: str

class ServiceTabungResponse(BaseModel):
    code: int
    no_rekening: str
    saldo: str

class ServiceTarikResponse(BaseModel):
    code: int
    no_rekening: str
    saldo: str

class SaldoResponse(BaseModel):
    saldo: str

#Error Schemas
class ErrorResponse(BaseModel):
    code: int
    remark: str
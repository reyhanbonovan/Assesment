import os
from dotenv import load_dotenv
load_dotenv()

class Config :
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "8080"))
    app_worker = int(os.getenv("APP_WORKER", "1"))

    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "postgres")
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASS", "admin")

    param_error = {
        "nik_hp_exist": [400, "NIK atau No HP sudah digunakan"],
        "rekening_exist": [400, "No Rekening sudah digunakan"],
        "sisa_saldo": [400, "Sisa saldo tidak cukup"],
        "rekening_no_exist": [400, "No Rekening tidak ditemukan"]
    }
    
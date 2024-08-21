class AppException(Exception):
    def __init__(self,  code: int, remark: str):
        self.code = code
        self.remark = remark
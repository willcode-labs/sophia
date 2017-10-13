from api.Model.ExceptionLog import ExceptionLog as ModelExceptionLog

class ExceptionLog():
    def __init__(self,request,model_login,model_login_client,**kwargs):
        self.request = request
        self.model_login = model_login
        self.model_login_client = model_login_client
        self.message = None
        self.description = None
        self.trace = None

        for key in kwargs:
            setattr(self,key,kwargs[key])

        if not self.message:
            raise Exception('Dados insuficientes para salvar um erro de excessão!')

        self.write()

    def __str__(self):
        return str(self.message)

    def write(self):
        self.exceptionLog()

    def exceptionLog(self):
        try:
            model_exception_log = ModelExceptionLog.objects.create(self.request,self.model_login,self.model_login_client,
                message=self.message,
                description=self.description,
                trace=self.trace)

        except Exception as error:
            return False

        return model_exception_log

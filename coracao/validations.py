from coracao.models import CoracaoModel

class CardiacoValidation:
    def __init__(self):
        self.__age = 0
        self.__sex = ''
        self.__chest_pain_type = ''
        self.__resting_bp = 0
        self.__cholesterol = 0
        self.__fastingBS = '0'
        self.__resting_ecg = ''
        self.__max_hr = 0
        self.__exercise_angina = ''
        self.__oldpeak = 0.0
        self.__st_slope = ''

    def set_idade(self, idade):
        if idade <= 0:
            raise ValueError("Idade deve ser maior que zero.")
        self.__age = idade

    def set_sexo(self, sexo):
        if sexo not in ['M', 'F']:
            raise ValueError("Sexo deve ser 'M' ou 'F'.")
        self.__sex = sexo

    def set_tipo_dor_peito(self, tipo):
        if tipo not in ['TA', 'ATA', 'NAP', 'ASY']:
            raise ValueError("Tipo de dor inválido.")
        self.__chest_pain_type = tipo

    def set_pressao_repouso(self, valor):
        self.__resting_bp = valor

    def set_colesterol(self, valor):
        self.__cholesterol = valor

    def set_jejum_acima_120(self, valor):
        if str(valor) not in ['0', '1']:
            raise ValueError("Jejum deve ser '0' ou '1'.")
        self.__fastingBS = str(valor)

    def set_ecg(self, valor):
        self.__resting_ecg = valor

    def set_freq_maxima(self, valor):
        self.__max_hr = valor

    def set_angina_exercicio(self, valor):
        if valor not in ['Y', 'N']:
            raise ValueError("Valor inválido para angina de exercício.")
        self.__exercise_angina = valor

    def set_oldpeak(self, valor):
        self.__oldpeak = valor

    def set_inclinacao_st(self, valor):
        self.__st_slope = valor

    def to_model(self):
        obj = CoracaoModel()
        obj.age = self.__age
        obj.sex = self.__sex
        obj.chest_pain_type = self.__chest_pain_type
        obj.resting_bp = self.__resting_bp
        obj.cholesterol = self.__cholesterol
        obj.fastingBS = self.__fastingBS
        obj.resting_ecg = self.__resting_ecg
        obj.max_hr = self.__max_hr
        obj.exercise_angina = self.__exercise_angina
        obj.oldpeak = self.__oldpeak
        obj.st_slope = self.__st_slope
        return obj

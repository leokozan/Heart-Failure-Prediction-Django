from django.views import View
from django.shortcuts import render
from coracao.models import CoracaoModel
from coracao.validations import CardiacoValidation 
import traceback
from django.shortcuts import redirect
import pickle
import os
import pandas as pd

class CoracaoCreateView(View):
    def get(self, request):
        return render(request, 'coracao/form.html')

    def post(self, request):
        try:
            age = int(request.POST.get('age'))
            sex = 1 if request.POST.get('sex') == 'M' else 0  # M:1 | F:0

            chest_pain_map = {'ASY': 0.0, 'ATA': 1.0, 'NAP': 2.0, 'TA': 3.0}
            chest_pain_type = chest_pain_map[request.POST.get('chest_pain_type')]

            resting_bp = int(request.POST.get('resting_bp'))
            cholesterol = int(request.POST.get('cholesterol'))
            fastingBS = int(request.POST.get('fastingBS'))

            ecg_map = {'Normal': 1.0, 'ST': 2.0, 'LVH': 3.0}
            resting_ecg = ecg_map[request.POST.get('resting_ecg')]

            max_hr = int(request.POST.get('max_hr'))
            exercise_angina = 1 if request.POST.get('exercise_angina') == 'Y' else 0

            oldpeak = float(request.POST.get('oldpeak'))

            st_slope_map = {'Down': 0.0, 'Flat': 1.0, 'Up': 2.0}
            st_slope = st_slope_map[request.POST.get('st_slope')]

            features = [[
                age,
                sex,
                chest_pain_type,
                resting_bp,
                cholesterol,
                fastingBS,
                resting_ecg,
                max_hr,
                exercise_angina,
                oldpeak,
                st_slope
            ]]

            model_path = os.path.join('hearth_model/model.pkl')
            with open(model_path, 'rb') as f:
                model = pickle.load(f)

            prediction = model.predict(features)
            print(prediction)
            heart_disease = int(prediction[0])  # 0 ou 1
            coracao = CardiacoValidation()
            coracao.set_idade(age)
            coracao.set_sexo(request.POST.get('sex'))
            coracao.set_tipo_dor_peito(request.POST.get('chest_pain_type'))
            coracao.set_pressao_repouso(resting_bp)
            coracao.set_colesterol(cholesterol)
            coracao.set_jejum_acima_120(request.POST.get('fastingBS'))
            coracao.set_ecg(request.POST.get('resting_ecg'))
            coracao.set_freq_maxima(max_hr)
            coracao.set_angina_exercicio(request.POST.get('exercise_angina'))
            coracao.set_oldpeak(oldpeak)
            coracao.set_inclinacao_st(request.POST.get('st_slope'))
            model_instance = coracao.to_model()
            model_instance.heart_disease = heart_disease
            model_instance.save()
            context = {'success': True, 'result': heart_disease}
        except Exception as e:
            import traceback
            traceback.print_exc()
            context = {
                'success': False,
                'error': str(e)
            }

        return render(request, 'coracao/form.html', context)
class CoracaoListaView(View):
    def get(self,request):
        pacientes = CoracaoModel.objects.all()
        return render(request, 'coracao/lista.html', {'pacientes': pacientes})
    
class CoracaoEditView(View):
    def get(self,request,id):
        paciente = CoracaoModel.objects.filter(id=id).first()
        return render(request, 'coracao/edit.html', {'paciente': paciente})
    def post(self, request, id):
        paciente = CoracaoModel.objects.get(id=id)
        try:
            validador = CardiacoValidation()
            validador.set_idade(int(request.POST.get('age')))
            validador.set_sexo(request.POST.get('sex'))
            validador.set_tipo_dor_peito(request.POST.get('chest_pain_type'))
            validador.set_pressao_repouso(int(request.POST.get('resting_bp')))
            validador.set_colesterol(int(request.POST.get('cholesterol')))
            validador.set_jejum_acima_120(request.POST.get('fastingBS'))
            validador.set_ecg(request.POST.get('resting_ecg'))
            validador.set_freq_maxima(int(request.POST.get('max_hr')))
            validador.set_angina_exercicio(request.POST.get('exercise_angina'))
            validador.set_oldpeak(float(request.POST.get('oldpeak')))
            validador.set_inclinacao_st(request.POST.get('st_slope'))
            dados_validados = validador.to_model()
            paciente.age = dados_validados.age
            paciente.sex = dados_validados.sex
            paciente.chest_pain_type = dados_validados.chest_pain_type
            paciente.resting_bp = dados_validados.resting_bp
            paciente.cholesterol = dados_validados.cholesterol
            paciente.fastingBS = dados_validados.fastingBS
            paciente.resting_ecg = dados_validados.resting_ecg
            paciente.max_hr = dados_validados.max_hr
            paciente.exercise_angina = dados_validados.exercise_angina
            paciente.oldpeak = dados_validados.oldpeak
            paciente.st_slope = dados_validados.st_slope

            paciente.heart_disease = int(request.POST.get('heart_disease')) 

            paciente.save()

            return redirect('lista_pacientes')

        except Exception as e:
            traceback.print_exc()

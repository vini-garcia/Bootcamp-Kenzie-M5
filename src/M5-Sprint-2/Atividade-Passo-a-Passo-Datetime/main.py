from datetime import datetime, timedelta


STR_FORMATACAO = '%d/%m/%y %H:%M:%S'

exame_realizado_em = datetime.now()

# print(exame_realizado_em)

data_exame_str = exame_realizado_em.strftime(STR_FORMATACAO)

# print(data_exame_str)

TEMPO_RESULTADO_EXAME = timedelta(days=2)

# print(TEMPO_RESULTADO_EXAME)

previsao_resultado = exame_realizado_em + TEMPO_RESULTADO_EXAME

# print(previsao_resultado)

previsao_de_entrega_str = previsao_resultado.strftime("%d/%m/%y %H:%M:%S")

# print(previsao_de_entrega_str)

# print(f'Data de realização do exame: {data_exame_str}\n\
# Previsão de entrega do resultado: {previsao_de_entrega_str}')

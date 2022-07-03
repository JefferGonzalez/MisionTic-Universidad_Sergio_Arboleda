distancia , velocidad , tiempo = input().split()
velocidad_media = ((int(distancia))/1000) / (int(tiempo)/3600)
status_negative = float(distancia) > 0 and float(velocidad) > 0 and float(velocidad) > 0
response = 'ERROR' if ((status_negative != True)  ) else 'OK'
if(response == 'OK' ) :
    response = 'OK' if((velocidad_media) < float(velocidad)) else 'MULTA'
if(response == 'MULTA'):
    response = 'MULTA' if(((velocidad_media-float(velocidad)) < (float(velocidad)*0.20)) and ((velocidad_media*1.20) >= (float(velocidad))) ) else 'CURSO SENSIBILIZACION'
print(response)
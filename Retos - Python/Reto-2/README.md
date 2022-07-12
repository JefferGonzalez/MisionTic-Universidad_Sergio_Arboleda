### Cálculo de Multas
<p>
    Debido a la alta accidentalidad presentada en el último año en las carreteras del territorio nacional, el Gobierno Colombiano ha decidido implementar controles que permitan sancionara a los conductores que no respeten los límites de velocidad establecidos por los organismos de control. Con este fin, el Ministerio de Transporte ha decidido implementar radares de tramo en las carreteras con mayores índices de accidentalidad en el país.
</p>
<p>
    Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo. Estos radares no miden la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un conductor en un trayecto con una longitud determinada.
</p>
<p>
    La interpretación del funcionamiento de los radares es simple: si colocamos las cámaras separadas 10 Km en un tramo cuya velocidad máxima es de 110 Km/h y un conductor tarda 5 minutos en ser visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km/h, y por tanto, en algún sitio ha superado la velocidad permitida.
</p>
<p>
    Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras. Su misión es crear un programa en Python que permita saber si un conductor debe ser multado o no.
</p>

<table>
    <tr>
        <th>ENTRADA</th>
        <td>
            El programa recibirá 3 parámetros:
            <ul>
                <li>La distancia en metros que separa dos cámaras</li>
                <li>La velocidad máxima permitida en ese tramo en (Km/h)</li>
                <li>El tiempo en segundos que tarda el conductor en recorrer el trayecto</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>SALIDA</th>
        <td>
            El programa imprimirá una línea indicando si el conductor debe ser multado o no.
            </br>
            Se debe considerar lo siguiente:
            <ul>
                <li>Imprimirá 'OK' si el conductor no superó la velocidad máxima.</li>
                <li>Imprimirá 'MULTA' si se superó la velocidad máxima en menos de un 20% de la velocidad permitida.</li>
                <li>Imprimirá 'CURSO SENSIBILIZACION' si la velocidad fue superada en un 20% o más de la velocidad permitida. En este caso además de la multa deberá realizar un curso de sensibilización.</li>
                <li>Debido a que los sistemas pueden fallar y registrar valores errados (por ejemplo, indicando que el tiempo que ha tardado el conductor es negativo). En esos casos, se deberá imprimir 'ERROR'</li>
            </ul>
        </td>
    </tr>
</table>

### Casos de prueba:

<table>
    <tr>
        <th>ENTRADA</th>
        <th>SALIDA</th>
    </tr>
    <tr>
        <td>9165 110 300</td>
        <td>OK</td>
    </tr>
    <tr>
        <td>9165 110 299</td>
        <td>MULTA</td>
    </tr>
    <tr>
        <td>1000 -50 -100</td>
        <td>ERROR</td>
    </tr>
    <tr>
        <td>12000 100 359</td>
        <td>CURSO SENSIBILIZACION</td>
    </tr>
</table>
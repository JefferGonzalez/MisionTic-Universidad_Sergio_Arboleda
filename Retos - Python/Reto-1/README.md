### Cálculo del Salario
<p>
    Un empleado de una compañía tiene dudas sobre si los pagos que le realiza la empresa de manera mensual son correctos. Con el propósito de aclarar sus inquietudes y verificar si los descuentos realizados son acordes a lo exigido por la ley, decide construir un programa en Python que le permita verificar el valor que debería ser pagado. Después de consultar sobre la normatividad colombiana y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:
</p>

<ul>
    <li>El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 192. Este valor corresponde a la jornada laboral establecida en el contrato (48 horas a la semana y 4 semanas al mes).</li>
    <li>Las horas extras se liquidan con un recargo del 25% sobre el valor de una hora normal.</li>
    <li>Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones del 5% del salario base.</li>
    <li>El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).</li>
    <li>Se descontará 3.5% del salario total antes de descuentos para el plan obligatorio de salud.</li>
    <li>Se descontará 4% del salario total antes de descuentos para el aporte a pensión.</li>
    <li>Se descontará 1% del salario total antes de descuentos para caja de compensación.</li>
</ul>

<p>
Luego de considerar toda esta información, el empleado decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos.
</p>

<table>
    <tr>
        <th>ENTRADA</th>
        <td>
            El programa recibirá 3 parámetros:
            <ul>
                <li>El salario base del empleado</li>
                <li>La cantidad de horas extras se representa a través de un número entero positivo. En caso de no de realizar horas extras durante el mes, se ingresará el valor 0.</li>
                <li>Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>SALIDA</th>
        <td>
            El programa debe imprimir el valor a pagar al empleado luego de realizar los descuentos de ley.
            </br>
            El resultado debe imprimirse con un número decimal.
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
        <td>1000000 0 0</td>
        <td>915000.0</td>
    </tr>
    <tr>
        <td>2355255 2 1</td>
        <td>2290871.9</td>
    </tr>
</table>
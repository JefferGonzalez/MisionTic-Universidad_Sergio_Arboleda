### Enunciado

### Detección de fallas en una línea de producción.

<p>
    En una fábrica de baldosas de cerámica se producen por día una gran cantidad de este producto. Es importante hacer control de calidad sobre el producto. Este control consiste en revisar si en un lote de N baldosas hay baldosas defectuosas (puede variar la textura o el color). La solicitud del gerente de la planta es que se construya un programa en Python que pueda detectar la cantidad de baldosas defectuosas en una de las líneas de producción de la fábrica.
</p>

<p>
Para detectar si una baldosa es diferente a otra, un sensor escanea las baldosas y si hay alguna diferencia, guarda un registro en la memoria. La memoria del sensor está limitada por la cantidad de baldosas que se producen en un intervalo de tiempo determinado.
</p>

<table>
    <tr>
        <th>ENTRADA</th>
        <td>
            La entrada estará conformada por dos líneas:
            <ul>
                <li>La primera línea aparecerá dos números N y K que indican el número de baldosas a revisar y el número de baldosas que el sensor es capaz de guardar (1≤N≤1000,1≤K≤1000).</li>
                <li>La segunda línea contiene M números (entre 1 y 100) separados por espacios que representan las baldosas revisadas por el sensor.</li>
                <li>Las baldosas se consideran defectuosas si están representados por el mismo número.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>SALIDA</th>
        <td>
            El programa imprimirá tres números separados por un espacio.
            <ul>
                <li>El primero representará el número total de fallas detectadas.</li>
                <li>El segundo representará la cantidad de fallas detectadas por el sensor considerando que al revisar una baldosa solo es capaz de guardar las K baldosas anteriores.</li>
                <li>El tercero representa la cantidad de baldosas revisadas por el sensor.</li>
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
        <td>
            5 1
            </br>
            1 2 3 1 2
        </td>
        <td>2 0 5</td>
    </tr>
    <tr>
        <td>
            5 2
            </br>
            1 2 3 1 2
        </td>
        <td>2 0 5</td>
    </tr>
    <tr>
        <td>
            5 3
            </br>
            1 2 3 1 2
        </td>
        <td>2 1 5</td>
    </tr>
</table>
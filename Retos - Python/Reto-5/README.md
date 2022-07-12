### Aplicación de gestión de inventarios.

<p>
    Una tienda vende diferentes productos, usualmente frutas, dulces y algunos tipos de carne. Con el propósito de mejorar el control sobre las ventas y el inventario de la tienda, el gerente decide construir una aplicación que le permita almacenar la información de los productos y realizar algunos cálculos sobre los datos.
</p>

<p>
En la primera parte del reto se debe construir una base de datos que almacene la información de los productos disponibles en la tienda. La base de datos será representada mediante un diccionario de Python llamado productos que tendrá por llave el código del producto y por valor una lista formada por los atributos: nombre, precio e inventario. La siguiente tabla presenta los productos disponibles a la fecha.
</p>

<table>
    <thead>
        <th>código</th>
        <th>nombre</th>
        <th>precio</th>
        <th>inventario</th>
    </thead>
    <tbody>
        <tr>
            <th>1</th>
            <td>Manzanas</td>
            <td>5000.0</td>
            <td>25</td>
        </tr>
        <tr>
            <th>2</th>
            <td>Limones</td>
            <td>2300.0</td>
            <td>15</td>
        </tr>
        <tr>
            <th>3</th>
            <td>Peras</td>
            <td>2700.0</td>
            <td>33</td>
        </tr>
        <tr>
            <th>4</th>
            <td>Arandanos</td>
            <td>9300.0</td>
            <td>5</td>
        </tr>
        <tr>
            <th>5</th>
            <td>Tomates</td>
            <td>2100.0</td>
            <td>42</td>
        </tr>
        <tr>
            <th>6</th>
            <td>Fresas</td>
            <td>4100.0</td>
            <td>3</td>
        </tr>
        <tr>
            <th>7</th>
            <td>Helado</td>
            <td>4500.0</td>
            <td>41</td>
        </tr>
        <tr>
            <th>8</th>
            <td>Galletas</td>
            <td>500.0</td>
            <td>8</td>
        </tr>
        <tr>
            <th>9</th>
            <td>Chocolates</td>
            <td>3500.0</td>
            <td>80</td>
        </tr>
        <tr>
            <th>10</th>
            <td>Jamon</td>
            <td>15000.0</td>
            <td>10</td>
        </tr>
    </tbody>
</table>

<p>
    Es necesario construir 3 funciones que representen las operaciones de: AGREGAR, ACTUALIZAR y BORRAR los productos disponibles. Se debe implementar una función independiente por cada una de las acciones mencionadas. En este caso, para poder realizar las operaciones de ACTUALIZAR o BORRAR es necesario especificar todos los atributos del producto.
</p>

<p>
    Adicionalmente, se está interesado en analizar los datos de los productos disponibles y conocer: el nombre del producto con el precio mayor; el nombre del producto con el precio menor; el promedio de precios de todos los productos y el valor total del inventario a la fecha. Este último se obtiene multiplicando el precio de cada producto por el inventario disponible y luego sumando todos los resultados. Por ejemplo, al calcular estos 4 valores para los datos disponibles en la anterior tabla obtendríamos:
</p>

<ul>
    <li>Producto precio mayor: Jamon</li>
    <li>Producto precio menor: Galletas</li>
    <li>Promedio de precios: 4900.0</li>
    <li>Valor del inventario: 101410.0</li>
</ul>

<table>
    <tr>
        <th>ENTRADA</th>
        <td>
            Cada uno de los casos de prueba estará compuesto por dos líneas.
            <ul>
                <li>
                    La primera línea estará formada por una cadena de texto que identifica la operación a realizar.  En este caso, las operaciones validas son:
                    <ul>
                        <li>ACTUALIZAR</li>
                        <li>BORRAR</li>
                        <li>AGREGAR</li>
                    </ul>
                </li>
                <li>
                    La segunda línea estará formada por 4 valores (código, nombre, precio, inventario) que representan el producto sobre el cual se quiere realizar la operación.
                </li>
                <li>
                    En el caso de la operación ACTUALIZAR la segunda línea debe contener el código y los nuevos valores del producto
                </li>
                <li>
                    En el caso de la operación BORRAR se deben especificar todos los atributos del producto a eliminar
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>SALIDA</th>
        <td>
            <ul>
                <li>
                    La salida estará representada por una única línea formada por cuatro valores:
                    <ul>
                        <li>Nombre del producto con el precio mayor</li>
                        <li>Nombre del producto con el precio menor</li>
                        <li>Promedio de precios</li>
                        <li>Valor del inventario</li>
                    </ul>
                </li>
                <li>
                    Estos 4 valores deben imprimirse después de realizar las operaciones solicitadas en la entrada de datos.
                </li>
                <li>Los valores numéricos deben imprimirse con un número decimal.</li>
                <li>
                    En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el código del producto no se encuentra en la base de datos), se debe imprimir 'ERROR'.
                </li>
                <li>
                    En caso de solicitar AGREGAR un producto cuyo código ya existe en la base de datos se debe imprimir 'ERROR'.
                </li>
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
            AGREGAR
            </br>
            11 Melon 70 13
        </td>
        <td>Jamon Melon 4460.9 1015010.0</td>
    </tr>
    <tr>
        <td>
            BORRAR
            </br>
            10 Jamon 15000 10
        </td>
        <td>Arandanos Galletas 3777.8 864100.0</td>
    </tr>
    <tr>
        <td>
            ACTUALIZAR
            </br>
            7 Helado 65000 11
        </td>
        <td>Helado Galletas 10950.0 1544600.0</td>
    </tr>
    <tr>
        <td>
            BORRAR
            </br>
            14 Maiz 45000 12
        </td>
        <td>ERROR</td>
    </tr>
</table>
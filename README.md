# C.A.J.A. del Olvido

Servicio para deshacerte de todo aquel recuerdo amargo que deseas eliminar.

## Requerimientos Backend

- Python >= 3.8
- Django==4.1.7
- django-cors-headers==3.14.0
- djangorestframework==3.14.0
- Pillow==9.4.0
- virtualenv==20.20.0

## Requerimientos Frontend

- NodeJS

## Instalacion Backend

1. Crear nuevo ambiente virtual

```bash
  cd codicon-event/backend && python3 -m venv /path/to/new/virtual/environment
```

2. Activar ambiente virtual

```bash
  source env/Scritps/activate
```

3. Instalar requerimientos del proyecto

```bash
pip install -r requirements.text
```

4. Correr las migraciones para la BD

```bash
python manage.py migrate
```

5. Iniciar el servidor desde la carpeta raiz

```bash
python manage.py runserver
```

Ya puedes acceder desde la URL: http://127.0.0.1:8000/

## Instalacion Frontend

1. Accede a la carpeta

```bash
  cd codicon-event/frontend
```

2. Instalar dependencias

```bash
  npm i
```

3. Iniciar el servidor desde la carpeta raiz

```bash
npm run dev
```

Ya puedes acceder desde la URL: http://127.0.0.1:3000/

## Funcionamiento

1. En la seccion Carta, escribiras todo lo que necesitas expresar luego solo presiona Enviar.

2. En la seccion Arreglar, subiras todas las fotos de esos recuerdos de los cuales te quieres deshacer luego solo presiona Enviar.

3. En la seccion Juntar, seleccionaras tu caja de preferencia podras seleccionar entre: Ataud, Caja fuerte,Caja de Regalo o una simple Caja de carton.

4. En la seccion Arreglar, decidiras cual sera el destino final de esta Caja del olvido podras seleccionar entre: Enterrar, Cremar, Regalar o Guardar.

5. En la seccion Datos Personales, deberas rellenar el formulario con tus datos correspondiente. Nombre, Apellido, Correo y numero telefonico.

6. En la seccion ¿A QUIEN LE ENVIARAS TUS RECUERDOS? Deberas colocar la informacion de la persona a quien enviaras todos tus recuerdos.

7. En la seccion de Pagos tendras que realizar tu pago de alguna de las formas mostradas sean Transferencia bancaria, Pago movil o via Zelle. Luego el numero de confirmacion de tu pago deberas introducirlo en Numero de Confirmacion a continuacion presiona Pagar, Y asi habras completado tu Caja del olvido.

8. Luego de confirmar tu pago, un agente de venta te contactara para afinar ultimos detalles de logistica.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Realizado por

- Equipo Code of Duty para el CODICON 2023.

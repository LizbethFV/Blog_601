import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash import html, register_page
from datetime import time
# Registra la página con un nombre y ruta personalizada
dash.register_page(__name__, path="/convenios", name="Convenios")

df_CECATI_13N = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20CECATI%2013%20numeralia.csv')
df_CECATI_13H = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20CECATI_13_Hor.csv')
df_CECATI_13I = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20CECATI_13_Instalaciones.csv')
df_CECATI_13NH = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/Horario_cecati13_Nu%20-%20CECATI%20-%20CECATI_13_Hor.csv')
Colores = ['#3B0815','#4F0527','#6C0A2B', '#85081E', '#9D0610', '#D90816', '#F72634','#F9626C', '#3B0815','#4F0527','#6C0A2B', '#85081E', '#9D0610', '#D90816', '#F72634','#F9626C']

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Grafica de la numeralia por año del CECATI 13
#Creamos una figura
categ13= ['Inscritos', 'Acreditados ','No acreditados','Deserción']
fig_CECATI13= go.Figure()

#Historico
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [df_CECATI_13N['Inscritos'].sum(), df_CECATI_13N['Acreditados '].sum(), df_CECATI_13N['No acreditados'].sum(), df_CECATI_13N['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=True,
    marker=dict(color=Colores),
    connector=dict(visible=False)
  )
)
#2019
CECATI13_19 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2019]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_19['Inscritos'].sum(), CECATI13_19['Acreditados '].sum(), CECATI13_19['No acreditados'].sum(), CECATI13_19['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))
#2020
CECATI13_20 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2020]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_20['Inscritos'].sum(), CECATI13_20['Acreditados '].sum(), CECATI13_20['No acreditados'].sum(), CECATI13_20['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))
#2021
CECATI13_21 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2021]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_21['Inscritos'].sum(), CECATI13_21['Acreditados '].sum(), CECATI13_21['No acreditados'].sum(), CECATI13_21['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))
#2022
CECATI13_22 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2022]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_22['Inscritos'].sum(), CECATI13_22['Acreditados '].sum(), CECATI13_22['No acreditados'].sum(), CECATI13_22['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))
#2023
CECATI13_23 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2023]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_23['Inscritos'].sum(), CECATI13_23['Acreditados '].sum(), CECATI13_23['No acreditados'].sum(), CECATI13_23['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))
#2024
CECATI13_24 = df_CECATI_13N[df_CECATI_13N['Ciclo escolar'] == 2024]
#Graficamos
fig_CECATI13.add_trace(go.Funnel(
    y = ['Inscritos', 'Acreditados ','No acreditados','Deserción'],
    x = [CECATI13_24['Inscritos'].sum(), CECATI13_24['Acreditados '].sum(), CECATI13_24['No acreditados'].sum(), CECATI13_24['Deserción'].sum()],
    text=categ13,
    textinfo = "text+value+percent initial",
    visible=False,
    marker=dict(color=Colores),
    connector=dict(visible=False)
))

#damos fromato
fig_CECATI13.update_layout(
    title='Resultados Académicos CECATI 13',
    title_font=dict(size=20, color='black'),
    font=dict(family='Verdana', size=15, color='black'),
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    yaxis_showticklabels=False
)
#Creamos el slider
Slider_CECATI13 = []
for i, label in enumerate(['2019-2024','2019','2020', '2021', '2022', '2023', '2024']):
    slider_CECATI13 = dict(
        method='update',
        label=label,
        args = [{"visible": [False] * len(fig_CECATI13.data)}]
    )
    slider_CECATI13['args'][0]['visible'][i] = True
    Slider_CECATI13.append(slider_CECATI13)

fig_CECATI13.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Año: '},
        steps=Slider_CECATI13
)]
)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#Infraestructura CECATI 13
#Para este mostraremos una tabla
CECATI13I = df_CECATI_13I['Especialidad'].unique()

#Creamos la tabla
tabla = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=["Especialidad", "Tipo de salón", "Num. salón", "Capacidad de alumnos"],
                fill_color='#9D0610',
                align='center',
                font=dict(color='white', size=15)
            ),
            cells=dict(
                values=[
                    df_CECATI_13I['Especialidad'],
                    df_CECATI_13I['Tipo de salón'],
                    df_CECATI_13I['Num. salón'],
                    df_CECATI_13I['Capacidad de alumnos']
                ],
                fill_color='white',
                align='left',
                font=dict(color='black', size=14)
            )
        )
    ]
)

# Título y ajustes
tabla.update_layout(
    title="Instalaciones del CECATI 13",
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='Verdana', size=15, color='black')
)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Horarios de los cursos que seleccionamos en este caso la especialidad tiene sus cursos
#Informatica
#Asistencia Educativa Inicial y Preescolar
#Uso de la Lengua Inglesa en Diversos Contextos
#Salon de usos multiples(Este no se usa por lo que no hay horario)
especialidades = ['Informática', 'Asistencia Educativa Inicial y Preescolar', 'Uso de la Lengua Inglesa en Diversos Contextos']
df_CECATI13_Hor = df_CECATI_13H[df_CECATI_13H['Especialidad'].isin(especialidades)]

# Creamos la figura
tabla_h = go.Figure()

#dias que colorearemos
columnas_horas = [
    'Lunes_Inicio', 'Lunes_Fin',
    'Martes_Inicio', 'Martes_Fin',
    'Miercoles_Inicio', 'Miercoles_Fin',
    'Jueves_Inicio', 'Jueves_Fin',
    'Viernes_Inicio', 'Viernes_Fin',
    'Sabado_Inicio', 'Sabado_Fin'
]

for especialidad in especialidades:
    df_filt = df_CECATI13_Hor[df_CECATI13_Hor['Especialidad'] == especialidad]

    #creamos una lista de listas con colores por columna
    colores_celdas = []

    #columnas fijas (no le ponemos color)
    colores_celdas.append(['white'] * len(df_filt))  #Cursos
    colores_celdas.append(['white'] * len(df_filt))  #Especialidad

    #Para cada columna de horario le podremos color a la celda
    for col in columnas_horas:
        colores_columna = [
            '#FFCCCC' if pd.notna(valor) else '#CCFFCC'  #rojo si est ocupado y verde si es null que seria libre
            for valor in df_filt[col]
        ]
        colores_celdas.append(colores_columna)

    #agregamos la tabla
    tabla_h.add_trace(
        go.Table(
            header=dict(
                values=['Cursos', 'Especialidad'] + columnas_horas,
                fill_color='#9A0924',
                align='center',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[df_filt['Cursos']] +
                       [df_filt['Especialidad']] +
                       [df_filt[col] for col in columnas_horas],
                fill_color=colores_celdas,
                align='left',
                font=dict(color='black', size=11)
            ),
            visible=False
        )
    )

#motramos la primera tabla
tabla_h.data[0].visible = True

#hacemos el dropdown
botones_dropdown = [
    dict(
        label=esp,
        method='update',
        args=[
            {'visible': [i == j for i in range(len(especialidades))]},
            {'title': f'Horarios de la especialidad: {esp}'}
        ]
    )
    for j, esp in enumerate(especialidades)
]

tabla_h.update_layout(
    width=1500,
    height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='Verdana', size=15, color='black'),
    updatemenus=[
        dict(
            buttons=botones_dropdown,
            direction="down",
            showactive=True,
            x=0.4,
            xanchor="left",
            y=1.12,
            yanchor="top"
        )
    ],
    title="Horarios de los Cursos del CECATI 13"
)
#------------------------------------------------------------------------------------------------------------
#Horario CECATI 13 modificados 
especialidades2 = ['Informática', 'Asistencia Educativa Inicial y Preescolar', 'Uso de la Lengua Inglesa en Diversos Contextos']
df_CECATI13_HorN = df_CECATI_13NH[df_CECATI_13NH['Especialidad'].isin(especialidades)]

# Especialidades a filtrar
especialidades2 = ['Informática', 'Asistencia Educativa Inicial y Preescolar', 'Uso de la Lengua Inglesa en Diversos Contextos']
df_CECATI13_HorN = df_CECATI_13NH[df_CECATI_13NH['Especialidad'].isin(especialidades2)]

# Columnas de horario
columnas_horas2 = [
    'Lunes_Inicio', 'Lunes_Fin',
    'Martes_Inicio', 'Martes_Fin',
    'Miercoles_Inicio', 'Miercoles_Fin',
    'Jueves_Inicio', 'Jueves_Fin',
    'Viernes_Inicio', 'Viernes_Fin',
    'Sabado_Inicio', 'Sabado_Fin'
]

# Días que se consideran en la tarde
dias_tarde = ['Jueves', 'Viernes', 'Sabado']

# Crear la figura
tabla_hn = go.Figure()

# Generar una tabla por cada especialidad
for especialidad2 in especialidades2:
    df_filt2 = df_CECATI13_HorN[df_CECATI13_HorN['Especialidad'] == especialidad2]

    # Crear colores por columna
    colores_celdas2 = []

    # Columnas fijas sin color
    colores_celdas2.append(['white'] * len(df_filt2))  # Cursos
    colores_celdas2.append(['white'] * len(df_filt2))  # Especialidad

    for col2 in columnas_horas2:
        colores_columna2 = []
        dia = col2.split('_')[0]

        for valor in df_filt2[col2]:
            if pd.isna(valor):
                color = '#CCFFCC'  # Verde (libre)
            else:
                try:
                    hora_valor = pd.to_datetime(valor).time()
                except Exception:
                    color = 'white'
                    colores_columna2.append(color)
                    continue

                if dia in dias_tarde:
                    if hora_valor >= time(15, 0):
                        color = '#CCFFCC'  # Verde (libre después de las 3 PM)
                    else:
                        color = '#FFCCCC'  # Rojo (ocupado antes de las 3 PM)
                else:
                    color = '#FFCCCC'  # Rojo (ocupado en días entre semana)

            colores_columna2.append(color)

        colores_celdas2.append(colores_columna2)

    # Agregar la tabla a la figura
    tabla_hn.add_trace(
        go.Table(
            header=dict(
                values=['Cursos', 'Especialidad'] + columnas_horas2,
                fill_color='#9A0924',
                align='center',
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[df_filt2['Cursos']] +
                       [df_filt2['Especialidad']] +
                       [df_filt2[col2] for col2 in columnas_horas2],
                fill_color=colores_celdas2,
                align='left',
                font=dict(color='black', size=11)
            ),
            visible=False
        )
    )

# Mostrar la primera tabla
tabla_hn.data[0].visible = True

# Crear botones del menú desplegable
botones_dropdown2 = [
    dict(
        label=esp,
        method='update',
        args=[
            {'visible': [i == j for i in range(len(especialidades2))]},
            {'title': f'Horarios de la especialidad: {esp}'}
        ]
    )
    for j, esp in enumerate(especialidades2)
]

# Actualizar diseño de la figura
tabla_hn.update_layout(
    width=1500,
    height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='Verdana', size=15, color='black'),
    updatemenus=[
        dict(
            buttons=botones_dropdown2,
            direction="down",
            showactive=True,
            x=0.4,
            xanchor="left",
            y=1.12,
            yanchor="top"
        )
    ],
    title="Nuevo Horario del CECATI 13"
)
#---------------------------------------------------------------------------------------------------------
layout = html.Div([

    html.H1("Hacia la optimización de espacios educativos: una propuesta de colaboración entre la UNRC y el CECATI", 
            className="animate-on-scroll",
            style={'font-family': 'Verdana', 'font-size': '25px', 'text-align': 'center','margin-bottom': '20px','font-weight': 'bold'}),
    html.P("Después de conocer el papel fundamental que desempeñan tanto la Universidad Nacional Rosario Castellanos (UNRC) como los Centros de Capacitación para el Trabajo Industrial (CECATI) en la formación académica y técnica de miles de estudiantes, este proyecto plantea una propuesta estratégica con el objetivo de optimizar el uso de los espacios educativos disponibles en la Ciudad de México. La finalidad es establecer un convenio de colaboración entre la UNRC y el CECATI, que permita utilizar las instalaciones de los centros CECATI como subsedes temporales o complementarias para actividades académicas de la UNRC. Esta propuesta se plantea sin interferir en el funcionamiento regular del CECATI, respetando sus horarios, especialidades y servicios.",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("¿Por qué es importante esta colaboración?", 
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("Actualmente, la demanda por un lugar en la educación superior sigue creciendo, y uno de los principales retos para la UNRC ha sido la disponibilidad de espacios físicos en sus sedes. Esta alianza permitiría:",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("• Ampliar la cobertura educativa de la UNRC sin necesidad de una inversión inmediata en nueva infraestructura.",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("• Acercar la educación a más estudiantes, especialmente a aquellos que enfrentan dificultades de movilidad o traslado hacia las unidades académicas principales.",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("• Fortalecer la vinculación institucional, aprovechando la experiencia técnica y operativa del CECATI, y fomentando el uso eficiente de los recursos públicos.",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
    html.P("• Con esta sinergia, la UNRC podría incrementar la oferta de lugares disponibles para nuevas y nuevos estudiantes, contribuyendo a una educación más accesible, equitativa y descentralizada.",
           className="animate-on-scroll",
           style={'font-family': 'Verdana', 'font-size': '16px', 'max-width': '1300px', 'line-height': '1.6', 'text-align': 'left', 'margin': '0 auto'}),
  
    #gráfica izquierda, texto derecha
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_CECATI13, className="animate-on-scroll")
        ], style={'flex': '1', 'padding': '10px'}),

        html.Div([
            html.H4("Caso de estudio: CECATI 13 como subsede potencial de la UNRC",
                    className="animate-on-scroll",
                    style={'font-family': 'Verdana', 'font-size': '18px','font-weight': 'bold'}),
            html.P("Como muestra para esta propuesta, se tomó la unidad CECATI 13, una de las más grandes y mejor equipadas de la Ciudad de México,. Esta unidad ha mostrado una evolución constante durante el periodo 2019–2024, tanto en matrícula como en diversificación de especialidades, lo cual la convierte en un excelente ejemplo para analizar la viabilidad del convenio. Cabe aclarar que el método que utlizaremos se puede aplicar a las demás instituciones.",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'})
        ], style={'flex': '1', 'padding': '10px', 'display': 'flex',
                  'flex-direction': 'column', 'justify-content': 'center'})
    ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '40px'}),

    #Texto izquierda, gráfica derecha
    html.Div([
        html.Div([
            html.H4("Infraestructura disponible",
                    className="animate-on-scroll",
                    style={'font-family': 'Verdana', 'font-size': '18px','font-weight': 'bold'}),
            html.P("El CECATI 13 cuenta con 22 especialidades, distribuidas en diversos salones y espacios, cuya capacidad varía según el tipo de curso que se imparta. Con base en un diagnóstico preliminar, se planteó una solicitud inicial de 3 salones y 1 laboratorio de cómputo, con el objetivo de utilizarlos en horarios no conflictivos con las actividades regulares del centro.",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
            html.P("Los espacios propuestos actualmente son utilizados para los siguientes cursos:",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
            html.P("• Informática",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
            html.P("• Asistencia Educativa Inicial y Preescolar",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
            html.P("• Uso de la Lengua Inglesa en Diversos Contextos",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
            html.P("• Salón de Usos Múltiples.",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'}),
        ], style={'flex': '1', 'padding': '10px', 'display': 'flex',
                  'flex-direction': 'column', 'justify-content': 'center'}),

        html.Div([
            dcc.Graph(figure=tabla, className="animate-on-scroll")
        ], style={'flex': '1', 'padding': '10px'})
    ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '40px'}),

    html.Div([
        html.Div([
            html.H4("Análisis de horarios y distribución",
                    className="animate-on-scroll",
                    style={'font-family': 'Verdana', 'font-size': '18px', 'font-weight': 'bold', 'text-align': 'center'}),
            html.P("Para garantizar que esta colaboración no interfiera con el funcionamiento habitual del CECATI, se realizó un análisis detallado de la distribución de horarios por especialidad. Se identificaron los días y franjas horarias con mayor ocupación, así como aquellos con menor demanda, lo cual permite definir con mayor precisión cuándo y cómo se podrían utilizar los espacios disponibles sin afectar a los cursos en curso.",
               className="animate-on-scroll",    
               style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1000px', 'margin': '0 auto'}),
            html.P("Este estudio es fundamental para construir un modelo de uso compartido de infraestructura, donde ambas instituciones se beneficien: la UNRC ampliando su capacidad para atender a más estudiantes, y el CECATI fortaleciendo su rol como centro estratégico de formación y vinculación",
               className="animate-on-scroll",
               style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1000px', 'margin': '0 auto'})
        ], style={'padding': '10px'}),

        html.Div([
            dcc.Graph(figure=tabla_h, className="animate-on-scroll")
            ],  style={
                  'padding': '0px',
                  'overflow-x': 'hidden',
                  'margin-bottom': '0px',  # elimina espacio debajo
                  'height': 'auto'         # asegura que no fije altura extra
})
            
        ]),
     html.Div([
         html.H4("Coordinación de horarios para la implementación del convenio",
                 className="animate-on-scroll",
                 style={'font-family': 'Verdana', 'font-size': '18px', 'font-weight': 'bold', 'text-align': 'center'}),
         html.P("Una vez identificados los salones y horarios disponibles en el CECATI 13, el siguiente paso fue determinar cuál de los turnos universitarios sería el más adecuado para aprovechar esos espacios sin afectar las actividades del centro.",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("Durante este año 2025, la Universidad Rosario Castellanos opera con tres turnos principales:",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("• Matutino: 7:00 a 11:00",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("• Matutino-Intermedio: 11:00 a 15:00",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("• Vespertino: 15:00 a 19:00",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("Además, se ha implementado una nueva modalidad de estudio denominada Presencial-Dual, la cual distribuye las sesiones en tres días presenciales y tres días en línea, permitiendo mayor flexibilidad y optimización del uso de espacios físicos.",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.H4("Horario acordado",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto','font-weight': 'bold'}),
         html.P("Tomando en cuenta esta modalidad, así como la disponibilidad real del CECATI 13, se logró un ajuste en su calendario interno que permite que la Universidad utilice sus instalaciones los siguientes días y horarios:",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("• Jueves, Viernes y Sábado",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("•Turno vespertino",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("• De 15:00 a 19:00 horas",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("Este horario coincide con los días de menor demanda en las especialidades impartidas en el CECATI, lo cual minimiza el impacto en sus actividades regulares, mientras que la universidad puede ampliar su oferta educativa sin necesidad de infraestructura adicional propia.",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.P("A continuación, se presenta un prototipo del nuevo esquema de distribución de horarios, donde se visualiza claramente la convivencia armónica entre ambas instituciones en un mismo espacio físico.",
            className="animate-on-scroll",    
            style={'font-family': 'Verdana', 'font-size': '16px', 'text-align': 'justify', 'max-width': '1200px', 'margin': '0 auto'}),
         html.Div([
            dcc.Graph(figure=tabla_hn, className="animate-on-scroll")
            ],  style={
                'padding': '0px',
                'overflow-x': 'hidden'})
         ]),
     html.Div([
         html.H3("Convenios Educativos",
                 className="animate-on-scroll",
                 style={'font-family': 'Verdana', 'font-size': '18px', 'font-weight': 'bold', 'text-align': 'center'}),
         html.P("Aquí puedes descargar el documento completo del convenio:",
                className="animate-on-scroll",
                style={'font-family': 'Verdana', 'font-size': '18px', 'font-weight': 'bold', 'text-align': 'center'}),
    
         html.A("📄 Descargar PDF del Convenio", 
                href="/assets/CONVENIO DE COLABORACIÓN ENTRE LA UNIVERSIDAD NACIONAL ROSARIO CASTELLANOS Y EL CENTRO DE CAPACITACIÓN PARA EL TRABAJO INDUSTRIAL NÚMERO 13 PARA EL USO DE INSTALACIONES.pdf", 
                target="_blank",
                download='CONVENIO DE COLABORACIÓN ENTRE LA UNIVERSIDAD NACIONAL ROSARIO CASTELLANOS Y EL CENTRO DE CAPACITACIÓN PARA EL TRABAJO INDUSTRIAL NÚMERO 13 PARA EL USO DE INSTALACIONES.pdf',
                style={"fontSize": "18px", "color": "blue", "textDecoration": "underline"}),

], style={'text-align': 'center'})

    ])

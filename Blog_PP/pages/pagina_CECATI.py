import dash
from dash import html, dcc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash import html, register_page

#Registrar la segunda pagina
dash.register_page(__name__, path="/CECATI", name="CECATI", order=2)

df_CECATI_OA = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20Numeralia%20inscritos-acreditados%20.csv')
df_CECATI_CE = pd.read_csv('https://raw.githubusercontent.com/LizbethFV/Bases_de_Datos_P.P_601/refs/heads/main/CECATI%20-%20Especialidades.csv')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# @title Grafica de matricula del CECATI por año
#Seleccionamos el año 2019
df_CECATI_OA2019 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2019]
#2020
df_CECATI_OA2020 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2020]
#2021
df_CECATI_OA2021 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2021]
#2022
df_CECATI_OA2022 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2022]
#2023
df_CECATI_OA2023 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2023]
#2024
df_CECATI_OA2024 = df_CECATI_OA[df_CECATI_OA['Periodo'] == 2024]

#Generamos una sola figura
fig_CECATI_M = go.Figure()

#Graficamo el historico
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA['Inscritos'].sum(), df_CECATI_OA['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=True,
    connector=dict(visible=False)
))
#Graficamos 2019
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2019['Inscritos'].sum(), df_CECATI_OA2019['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2020
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2020['Inscritos'].sum(), df_CECATI_OA2020['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2021
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2021['Inscritos'].sum(), df_CECATI_OA2021['Acreditados'].sum()],
    text = ["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))
#Graficamos 2022
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2022['Inscritos'].sum(), df_CECATI_OA2022['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))
#graficamos 2023
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2023['Inscritos'].sum(), df_CECATI_OA2023['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))
#graficamos 2024
fig_CECATI_M.add_trace(go.Funnel(
    y = ["Inscritos", "Acreditados"],
    x = [df_CECATI_OA2024['Inscritos'].sum(), df_CECATI_OA2024['Acreditados'].sum()],
    text=["Inscritos", "Acreditados"],
    textinfo = "text+value+percent initial",
    marker=dict(color=['#9D0610', '#D90816']),
    visible=False,
    connector=dict(visible=False)
))

#damos fromato
fig_CECATI_M.update_layout(
    title='Inscritos y Acreditados Historico y por Año del CECATI',
    title_font=dict(size=20, color='black'),
    font=dict(family='Verdana', size=15, color='black'),
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    yaxis_showticklabels=False
)
#Creamos el Slider
Slider_CECATI_M = []
for i, label in enumerate(['2019-2024','2019','2020', '2021', '2022', '2023', '2024']):
    slider_CECATI_M = dict(
        method='update',
        label=label,
        args = [{"visible": [False] * len(fig_CECATI_M.data)}]
    )
    slider_CECATI_M['args'][0]['visible'][i] = True
    Slider_CECATI_M.append(slider_CECATI_M)

fig_CECATI_M.update_layout(
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Año: '},
        steps=Slider_CECATI_M
)]
)
#---------------------------------------------------------------------------------------------------
#Especialidades por unidad academica
# en este caso haremos una tabla por unidad del CECATI
#Hacemos una lista de cecati
CECATI = df_CECATI_CE['CECATI'].unique()

#Creamos una figura
tab_CECATI = go.Figure()

for cecati in CECATI:
  CEATI_F = df_CECATI_CE[df_CECATI_CE['CECATI'] == cecati]

  #Creamos la tabla
  tab_CECATI.add_trace(
      go.Table(
          header=dict(
              values=['Especialidad', 'Clave', 'Modalidad'],
              fill_color=['#9D0610'],
              font=dict(color='white', family='Verdana'),
              align='center',
              line=dict(color='#ba181b', width=0)
          ),
          cells=dict(
              values=[CEATI_F['Especialidad'], CEATI_F['Clave'], CEATI_F['Modalidad']],
              fill_color='white',
              align='left',
              line=dict(color='#ba181b', width=0),
          ),
          visible=False
      )
      )
#Mostramos la primera tabla para que no se vea vacio
tab_CECATI.data[0].visible = True

#Creamos un dropdown
Boton= [
    dict(
        label=f"CECATI {cecati}",
        method="update",
        args=[{"visible": [k == j for k in range(len(CECATI))]}, {"title": f"Especialidades del CECATI {cecati}"}]
    )
    for j, cecati in enumerate(CECATI)
]
tab_CECATI.update_layout(
    width=900,
    height=500,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family='Verdana', size=15, color='black'),
    updatemenus = [
        dict(
            buttons=Boton,
            direction="down",
            showactive=True,
            x=0.5,
            xanchor="center",
            y=1.12,
            yanchor="top"
        )
    ],
    title="Especialidades de los CECATI en la CDMX"
)
#---------------------------------------------------------------------------------------------------------
layout = html.Div([
    html.Div([
        html.P('Elaborado por:',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','font-weight': 'bold','margin-bottom': '0px'}),
        html.P('Lizbeth Fernandez Viñas',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','font-weight': 'bold','margin-bottom': '0px'}),
        html.P('Isis Minerva Osorio Cano',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','font-weight': 'bold','margin-bottom': '0px'}),
        html.P('Rocio Olvera Guzmán',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','font-weight': 'bold','margin-bottom': '10px'}),
        html.P('Licenciatura en Ciencia de Datos para Negocios',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','font-weight': 'bold','margin-bottom': '10px'}),
        html.P('Publicado el 29 de mayo de 2025',
               style={'font-family': 'Verdana', 'font-size': '12px', 'text-align': 'left','margin-bottom': '20px','font-weight': 'bold'}),
    ]),
    html.Div([
        html.H1("CECATI: Capacitación técnica para el impulso laboral en México", 
                className="animate-on-scroll",
                style={'font-family': 'Verdana', 'font-size': '25px', 'text-align': 'center','margin-bottom': '20px','font-weight': 'bold'}
        ),
        html.P("La Dirección General de Centros de Formación para el Trabajo (DGCFT), a través de los Centros de Capacitación para el Trabajo Industrial (CECATI), ha jugado un papel fundamental en el fortalecimiento del capital humano del país. Estos centros, creados en 1976 como parte de una estrategia nacional, surgieron para responder a la creciente demanda de mano de obra especializada en distintas áreas industriales. Los CECATI son instituciones públicas dedicadas a ofrecer formación técnica de calidad, con un enfoque práctico. Sus programas están dirigidos a personas que buscan integrarse o mejorar su desempeño en los sectores productivo, público, privado y social. Una de sus principales fortalezas es la estructura de los cursos: aproximadamente el 80% del contenido es práctico y el 20% teórico, lo que permite a las y los estudiantes adquirir habilidades concretas desde el primer momento.",
               className="animate-on-scroll",
               style={'font-family': 'Verdana', 'font-size': '17px', 'max-width': '1200px', 'line-height': '1.6', 'text-align': 'center', 'margin': '0 auto'})
    ], style={'margin-top':'50px'}),
    #grafica izquierda texto derecha
    html.Div([
        html.Div([
            html.H4("Presencia en todo el país",
                    className="animate-on-scroll",
                    style={'font-family': 'Verdana', 'font-size': '18px','font-weight': 'bold'}),
            html.P("Actualmente, existen 201 unidades de CECATI distribuidas en toda la República Mexicana, de las cuales 32 se encuentran en la Ciudad de México. Cada centro ofrece distintas especialidades, dependiendo del número de salones, infraestructura y demanda local. Un dato interesante es que todos los CECATI cuentan al menos con un laboratorio de cómputo, lo que garantiza que los estudiantes tengan acceso a herramientas digitales durante su formación.",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'})
        ], style={'flex': '1', 'padding': '10px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),

        html.Div([
            dcc.Graph(figure=tab_CECATI,className="animate-on-scroll")
        ], style={'flex': '1', 'padding': '10px'})
    ], style={'display': 'flex', 'flex-direction': 'row','margin-bottom': '40px'}),
              
    #Gráfica derecha, texto izquierda
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_CECATI_M, className="animate-on-scroll")
        ], style={'flex': '1', 'padding': '10px'}),

        html.Div([
            html.H4("Impacto durante el periodo 2019–2024",
                    className="animate-on-scroll",
                    style={'font-family': 'Verdana', 'font-size': '18px','font-weight': 'bold'}),
            html.P("Entre los años 2019 y 2024, los CECATI registraron un total acumulado de 2,495,234 estudiantes inscritos a nivel nacional. De estos, el 83% logró acreditar satisfactoriamente sus cursos, reflejo del compromiso tanto del personal docente como del estudiantado. En la gráfica que se presenta a continuación, es posible observar la evolución de la matrícula durante este periodo, evidenciando la relevancia y el impacto de estos centros en la formación para el trabajo en México.",
                   className="animate-on-scroll",
                   style={'font-family': 'Verdana', 'font-size': '16px'})
        ], style={'flex': '1', 'padding': '10px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'})
    ], style={'display': 'flex', 'flex-direction': 'row',
              'margin-bottom': '40px'}),



])

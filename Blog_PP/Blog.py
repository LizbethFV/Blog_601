from dash import Dash, html, dcc, page_container, page_registry, Output, Input
import dash_bootstrap_components as dbc
import webbrowser
import threading
import time

Blog = Dash(__name__, use_pages=True, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    dbc.icons.BOOTSTRAP,
    '/assets/custom.css'
])

Colores_blog = {
    'sidebar_bg': '#860E38',
    'text_light': '#fcfcfc',
    'link_active_bg': '#FFFFFF',
    'link_hover_bg': '#333333',
    'main_content_bg': '#ffffff',
    'main_content_shadow': '#FFFFFF',
    'header_content_bg': '#283C55',
    'header_content_text': '#FFFFFF'
}

orden_paginas = [
    "/",         # Universidad Nacional Rosario Castellanos
    "/CECATI",   # CECATI
    "/convenios" # Convenios
]

Blog.layout = html.Div([
    
    # Barra lateral
    html.Div([
        html.Div([
            html.H3("Optimización de Espacios en la Universidad Nacional Rosario Castellanos",
                    className="d-inline-block align-middle",
                    style={'color': '#e2c78f'}),
            html.Hr(style={'border-top': '1px solid rgba(255,255,255,0.2)',
                           'margin-top': '10px',
                           'margin-bottom': '20px'})
        ], style={'padding-bottom': '10px', 'padding-top': '10px'}),

        html.H5("Menú",
                className="text-uppercase mb-3",
                style={'color': 'white', 'padding-left': '20px'}),
        dbc.Nav(
            [
                dbc.NavLink(
                    html.Div([page["name"]]),
                    href=page["relative_path"],
                    active="exact",
                    className="nav-link-sidebar"
                )
                for page in page_registry.values()
            ],
            vertical=True,
            pills=False,
            className="flex-column"
        ),

    ], style={
        'background-color': '#FFFFFF',
        'padding': '20px',
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'height': '100vh',
        'width': '250px',
        'z-index': 1000,
        'box-shadow': '2px 0 5px rgba(0,0,0,0.2)'
    }, id='sidebar-fixed'),

    # Contenido principal
    html.Div([
        dcc.Location(id='url', refresh=False),

        # Banner que se actualiza con imagen y texto
        html.Div([
            html.H1(id='banner-title')
        ], id='banner'),

        # Contenido de las páginas
        page_container
    ], style={
        'background-color': Colores_blog['main_content_bg'],
        'padding': '20px',
        'min-height': '100vh',
        'margin-left': '250px',
        'box-shadow': Colores_blog['main_content_shadow']
    })

], style={'overflow-x': 'hidden'})


# Callback para cambiar el fondo del banner y el texto del título
@Blog.callback(
    Output('banner', 'style'),
    Input('url', 'pathname')
)
def update_banner(pathname):
    # Diccionario de imágenes por ruta
    imagenes_pagina = {
        "/": 'UNRC.jpg',
        "/CECATI": 'CECATI.jpg',
        "/convenios": 'UNRC_CECATI.jpg'
    }     
    #Imagen por defecto
    imagen = imagenes_pagina.get(pathname, 'UNRC.jpg')

    estilo_banner = {
        'background-image': f'url("/assets/{imagen}")',
        'background-size': 'cover',
        'background-position': 'center',
        'padding': '300px 40px',
        'font-weight': 'bold',
        'font-size': '3rem',
        'color': 'white',
        'text-align': 'left',
        'margin-bottom': '10px',
        'box-shadow': '0 2px 4px rgba(0,0,0,0.1)'
    }

    return estilo_banner

#cambiamos el color de la barra lateral
@Blog.callback(
    Output('sidebar-fixed', 'style'),
    Input('url', 'pathname')
)
def update_sidebar_style(pathname):
    colores_lateral = {
        "/": '#691C32',
        "/CECATI": '#9F2241',
        "/convenios": '#841F3A'
    }  
    color_lateral = colores_lateral.get(pathname, '#630138')
    
    return {
        'background-color': color_lateral,
        'padding': '20px',
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'height': '100vh',
        'width': '250px',
        'z-index': 1000,
        'box-shadow': '2px 0 5px rgba(0,0,0,0.2)',
        'transition': 'background-color 0.5s ease'
    }

# Abrir navegador automáticamente
def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')


if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    Blog.run(debug=True)
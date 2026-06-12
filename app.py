import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Gabinete de Crisis Climática", page_icon="🌍", layout="centered")

# 2. Base de datos con tus 32 columnas
COLUMNAS_DATA = [
    {"id": 1, "titulo": "AHORA NADA SORPRENDE", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/ahora-nada-sorprende-785931"},
    {"id": 2, "titulo": "ANALOGIA DE LA QUINTA ESTACION", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/la-analogia-de-la-quinta-estacion-826746"},
    {"id": 3, "titulo": "APOSTANDOLE A LA REDUCCION DEL RIESGO", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/apostandole-la-reduccion-del-riesgo-de-desastres-763001"},
    {"id": 4, "titulo": "AVES QUE MIGRAN RADARES QUE LAS DETECTAN", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/aves-que-migran-radares-que-las-detectan-cristian"},
    {"id": 5, "titulo": "BALANCE DIFICIL DE OLVIDAR", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/balance-dificil-de-olvidar-779807"},
    {"id": 6, "titulo": "CAMBIOS CADA VEZ MÁS EVIDENTES Y PREOCUPANTES", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/cambios-cada-vez-mas-evidentes-y-preocupantes-794517"},
    {"id": 7, "titulo": "CONCLUYENTE Y NADA ALENTADOR", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/concluyente-y-nada-alentador-columna-de-christian"},
    {"id": 8, "titulo": "COP26 COMPROMISOS REALIZABLES", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/cop26-compromisos-realizables-columna-de-christian"},
    {"id": 9, "titulo": "CRISIS CLIMÁTICA: CAMBIO DE PARADIGMA", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/crisis-climatica-cambio-de-paradigma-720803"},
    {"id": 10, "titulo": "CUANDO DE RAYOS SE TRATA", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/cuando-de-rayos-se-habla-739516"},
    {"id": 11, "titulo": "DAÑOS QUE PUEDEN SER IRREPARABLES", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/danos-que-pueden-ser-irreparables-797734"},
    {"id": 12, "titulo": "DEFORESTANDO VIDA", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/deforestando-vida-722680"},
    {"id": 13, "titulo": "DÍA DEL MEDIO AMBIENTE EN MEDIO DE PREOCUPACIONES", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/dia-del-medio-ambiente-con-preocupaciones-822995"},
    {"id": 14, "titulo": "ES SUFICIENTE EL AGUA QUE TENEMOS", "url": "https://www.elheraldo.co/columnas-de-opinion/cristhian-euscategui/es-suficiente-el-agua-que-tenemos-714821"},
    {"id": 15, "titulo": "EXTRAÑO SOL", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/un-extrano-sol-728278"},
    {"id": 16, "titulo": "INCERTIDUMBRES AGROCLIMÁTICAS", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/las-incertidumbres-agroclimaticas-761342"},
    {"id": 17, "titulo": "INCIDENCIA DE LA NIÑA? BUENA PREGUNTA", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/incidencia-de-la-nina-801200"},
    {"id": 18, "titulo": "LA IMPORTANCIA DE LAS MEDICIONES EN FUNCIÓN DEL RIESGO", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/importancia-de-las-mediciones-en-funcion-del-riesgo-716813"},
    {"id": 19, "titulo": "LAS ALERTAS TEMPRANAS PARA SALVAR VIDAS", "url": "https://www.elheraldo.co/columnas-de-opinion/cristhian-euscategui/alertas-tempranas-para-salvar-vidas-706938"},
    {"id": 20, "titulo": "LOS DESASTRES NO SON NATURALES", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/los-desastres-no-son-naturales-807713"},
    {"id": 21, "titulo": "MÁS Y MEJOR INFORMACIÓN", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/mas-y-mejor-informacion-790939"},
    {"id": 22, "titulo": "MINERIA ILEGAL", "url": "https://www.elheraldo.co/columnas-de-opinion/mineria-ilegal-destruyendo-vida-746962"},
    {"id": 23, "titulo": "NIEVES NO TAN PERPETUAS", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/nieves-no-tan-perpetuas-743318"},
    {"id": 24, "titulo": "NUESTROS OCEANOS TODO UN PRIVILEGIO", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/nuestros-oceanos-todo-un-privilegio-734014"},
    {"id": 25, "titulo": "OLVIDAMOS LA LECCIÓN", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/olvidamos-la-leccion-730000"},
    {"id": 26, "titulo": "PRESENTE Y FUTURO CON CARA DE PASADO", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/presente-y-futuro-con-cara-de-pasado-804517"},
    {"id": 27, "titulo": "QUE TANTO CONOCEMOS DE CLIMA", "url": "https://www.elheraldo.co/columnas-de-opinion/que-tanto-conocemos-de-clima-705212"},
    {"id": 28, "titulo": "REPERCUSIONES DE UN CLIMA CAMBIANTE", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/repercusiones-de-un-clima-cambiante-columna-de-christian"},
    {"id": 29, "titulo": "RIESGOS CONCATENADOS AL ACECHO", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/riesgos-concatenados-al-acecho-732182"},
    {"id": 30, "titulo": "TODO CON PINZAS", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/todo-con-pinzas-columna-de-christian-euscategui-849135"},
    {"id": 31, "titulo": "UN POCO DE POLVO DEL SAHARA", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/un-poco-de-polvo-del-sahara-737702"},
    {"id": 32, "titulo": "VIENTOS CRUZADOS", "url": "https://www.elheraldo.co/columnas-de-opinion/christian-euscategui/vientos-cruzados-dedos-cruzados-718666"}
]

# 3. Inicializar el estado global compartido en el servidor
@st.cache_resource
def obtener_estado_gabinete():
    return {"asignaciones": {}}

estado_global = obtener_estado_gabinete()

# Inicializar las variables de la sesión individual de cada estudiante
if "mi_lectura_id" not in st.session_state:
    st.session_state["mi_lectura_id"] = None
if "mi_nombre" not in st.session_state:
    st.session_state["mi_nombre"] = ""

# 4. Interfaz de usuario
st.title("🌍 Asignación de Informes: Gabinete de Crisis")
st.markdown("### Maestría en Gestión del Riesgo y Cambio Climático")
st.write("Selecciona un informe técnico de la lista para preparar tu presentación oficial ante el comité.")

# Filtrar lecturas en tiempo real
lecturas_ocupadas = estado_global["asignaciones"]
lecturas_disponibles = [c for c in COLUMNAS_DATA if c["id"] not in lecturas_ocupadas]

st.divider()

# Caso A: El estudiante ya reservó una lectura en este dispositivo
if st.session_state["mi_lectura_id"] is not None:
    id_actual = st.session_state["mi_lectura_id"]
    nombre_actual = st.session_state["mi_nombre"]
    
    lectura_actual = next((c for c in COLUMNAS_DATA if c["id"] == id_actual), None)
    
    if lectura_actual:
        st.success(f"📋 **{nombre_actual}**, tu informe ya se encuentra reservado.")
        st.markdown(f"### 📖 Lectura asignada:\n**{lectura_actual['titulo']}**")
        st.markdown(f"[🔗 Haz clic aquí para abrir y leer tu columna en El Heraldo]({lectura_actual['url']})")
        
        st.info("""
        **Estructura de tu presentación ante el Gabinete:**
        \n*"Soy **[Tu Nombre]**, experto en **[Tu Profesión/Sector]**. El informe que analicé expone que el mayor riesgo latente es **X**... y mi expectativa en este curso es aprender a administrar/articular **Y**"*
        """)
    else:
        st.error("Hubo un problema al recuperar tu lectura. Por favor, solicita un reinicio.")

# Caso B: El estudiante aún no ha seleccionado lectura
else:
    st.subheader("1. Registra tus datos y elige un informe")
    
    if len(lecturas_disponibles) == 0:
        st.warning("¡Todas las lecturas disponibles ya han sido asignadas por tus compañeros!")
    else:
        with st.form("formulario_reserva"):
            # Ajuste solicitado: Indicación explícita de Nombre completo
            nombre_input = st.text_input("Nombre completo:")
            
            opciones_combo = {c["titulo"]: c["id"] for c in lecturas_disponibles}
            seleccion_titulo = st.selectbox("Selecciona una columna que esté disponible:", list(opciones_combo.keys()))
            
            boton_enviar = st.form_submit_button("Confirmar y Reservar Lectura")
            
            if boton_enviar:
                if not nombre_input.strip():
                    st.error("Por favor ingresa tu nombre completo antes de confirmar.")
                else:
                    id_seleccionado = opciones_combo[seleccion_titulo]
                    
                    # Transformación solicitada: Forzar MAYÚSCULAS fijas
                    nombre_mayusculas = nombre_input.strip().upper()
                    
                    if id_seleccionado in estado_global["asignaciones"]:
                        st.error("¡Vaya! Otro compañero acaba de seleccionar esa misma lectura. Por favor elige otra.")
                    else:
                        # Guardar en mayúsculas global y localmente
                        estado_global["asignaciones"][id_seleccionado] = nombre_mayusculas
                        st.session_state["mi_lectura_id"] = id_seleccionado
                        st.session_state["mi_nombre"] = nombre_mayusculas
                        st.rerun()

# 5. Consola de Monitoreo exclusiva para el Profesor (Consolidado)
st.divider()
with st.expander("⚙️ Consola de Monitoreo del Docente (Tiempo Real)"):
    st.write(f"**Lecturas asignadas:** {len(lecturas_ocupadas)} de {len(COLUMNAS_DATA)}")
    
    # Crear la lista para la tabla estructurada
    tabla_monitoreo = []
    for c in COLUMNAS_DATA:
        estado = lecturas_ocupadas.get(c["id"], "🟢 Disponible")
        tabla_monitoreo.append({"ID": c["id"], "Título de la Columna": c["titulo"], "Asignado a": estado})
    
    df_monitoreo = pd.DataFrame(tabla_monitoreo)
    st.table(df_monitoreo)
    
    # NUEVO: Botón para descargar el reporte consolidado del grupo en CSV
    st.subheader("📊 Descargar Resultados")
    csv_data = df_monitoreo.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar listado consolidado (CSV)",
        data=csv_data,
        file_name="consolidado_lecturas_maestria.csv",
        mime="text/csv"
    )
    
    # Botón maestro de reinicio
    st.subheader("🚨 Control de Aula")
    if st.button("⚠️ Reiniciar todas las asignaciones del salón"):
        estado_global["asignaciones"] = {}
        st.session_state["mi_lectura_id"] = None
        st.session_state["mi_nombre"] = ""
        st.rerun()
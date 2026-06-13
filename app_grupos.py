import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Consolidación de Grupos de Trabajo", page_icon="👥", layout="centered")

# 2. Listas de insumos oficiales
DEPARTAMENTOS = [
    "HUILA",
    "VALLE",
    "SANTANDER",
    "NARIÑO",
    "ANTIOQUIA",
    "EJE CAFETERO (RISARALDA-QUINDÍO-CALDAS)"
]

TEMAS = [
    "1. Planes Integrales de Gestión del Cambio Climático Territoriales",
    "2. Plan Nacional de Adaptación al Cambio Climático.",
    "3. Vulnerabilidad territorial al cambio climático.",
    "4. Acuerdo de París.",
    "5. Adaptación basada en comunidades.",
    "6. AR6 Synthesis Report: Climate Change 2022",
    "7. Globalización, ambiente y cambio climático",
    "8. Desarrollo humano y desarrollo sostenible"
]

# 3. Base de datos global compartida en el servidor
@st.cache_resource
def inicializar_base_datos_grupos():
    return {
        # Guarda las elecciones de cada uno de los 6 grupos
        "config_grupos": {i: {"departamento": None, "tema": None} for i in range(1, 7)},
        # Lista de estudiantes registrados
        "estudiantes": []
    }

db = inicializar_base_datos_grupos()

# 4. Interfaz de usuario
st.title("👥 Registro de Grupos y Temas de Exposición")
st.markdown("### Maestría en Gestión del Riesgo y Cambio Climático")
st.write("Por favor, coordina con tu equipo de trabajo. Un miembro del grupo registrará el territorio y tema asignado, y todos los integrantes deben matricular sus datos individuales.")

st.divider()

st.subheader("📝 Formulario de Registro")

# El estudiante selecciona primero su grupo establecido
numero_grupo = st.selectbox("Selecciona tu Número de Grupo:", list(range(1, 7)), index=0)

# Verificar si este grupo ya tomó decisiones de Departamento y Tema
grupo_configurado = db["config_grupos"][numero_grupo]["departamento"] is not None

if grupo_configurado:
    dept_asignado = db["config_grupos"][numero_grupo]["departamento"]
    tema_asignado = db["config_grupos"][numero_grupo]["tema"]
    st.info(f"ℹ️ **Información de Grupo Detectada:** El Grupo {numero_grupo} ya tiene asignado el departamento **{dept_asignado}** y el tema **{tema_asignado}**.")
else:
    st.warning(f"⚠️ **Grupo sin configurar:** Eres el primer integrante en registrarse del Grupo {numero_grupo}. Debes ingresar las elecciones concertadas por tu equipo.")

# Formulario para capturar los datos
with st.form("registro_estudiante"):
    
    # Datos personales solicitados por el docente
    nombre_input = st.text_input("Nombre completo (Obligatorio):")
    codigo_input = st.text_input("Código de estudiante:")
    correo_input = st.text_input("Correo electrónico:")
    celular_input = st.text_input("Número de celular:")
    
    # Si el grupo NO está configurado, le pide elegir de lo que quede disponible
    if not grupo_configurado:
        # Calcular depto y temas libres
        deptos_ocupados = [g["departamento"] for g in db["config_grupos"].values() if g["departamento"] is not None]
        temas_ocupados = [g["tema"] for g in db["config_grupos"].values() if g["tema"] is not None]
        
        deptos_libres = [d for d in DEPARTAMENTOS if d not in deptos_ocupados]
        temas_libres = [t for t in TEMAS if t not in temas_ocupados]
        
        st.markdown("---")
        st.markdown("#### Selecciones del Grupo")
        depto_seleccionado = st.selectbox("Selecciona el Departamento asignado a tu grupo:", deptos_libres)
        tema_seleccionado = st.selectbox("Selecciona el Tema de exposición de tu grupo:", temas_libres)
    else:
        # Si ya está configurado, heredamos internamente las variables
        depto_seleccionado = db["config_grupos"][numero_grupo]["departamento"]
        tema_seleccionado = db["config_grupos"][numero_grupo]["tema"]

    boton_guardar = st.form_submit_button("Confirmar Registro")

    if boton_guardar:
        if not nombre_input.strip():
            st.error("El nombre completo es obligatorio para poder realizar el registro.")
        else:
            # Forzar nombre completo a MAYÚSCULAS fijas
            nombre_mayusculas = nombre_input.strip().upper()
            
            # Si era el primero, guardamos la configuración para el grupo completo formalmente
            if not grupo_configurado:
                db["config_grupos"][numero_grupo]["departamento"] = depto_seleccionado
                db["config_grupos"][numero_grupo]["tema"] = tema_seleccionado
            
            # Registrar el estudiante en la lista general
            nuevo_estudiante = {
                "GRUPO": f"Grupo {numero_grupo}",
                "DEPARTAMENTO": depto_seleccionado,
                "TEMA": tema_seleccionado,
                "NOMBRE COMPLETO": nombre_mayusculas,
                "CÓDIGO": codigo_input.strip(),
                "CORREO": correo_input.strip(),
                "CELULAR": celular_input.strip()
            }
            
            db["estudiantes"].append(nuevo_estudiante)
            st.success(f"¡Excelente! **{nombre_mayusculas}** ha sido registrado con éxito en el {nuevo_estudiante['GRUPO']}.")
            st.rerun()

# 5. Consola del Docente para control de Aula y descarga del consolidado
st.divider()
with st.expander("⚙️ Consola de Monitoreo del Docente (Consolidado de Matrícula)"):
    
    if len(db["estudiantes"]) == 0:
        st.write("Aún no se han registrado estudiantes.")
    else:
        st.subheader("📊 Listado Completo del Grupo")
        # Convertir a DataFrame organizado
        df_consolidado = pd.DataFrame(db["estudiantes"])
        
        # Ordenar por grupo para facilitarte la lectura en Excel
        df_consolidado = df_consolidado.sort_values(by=["GRUPO", "NOMBRE COMPLETO"])
        
        # Mostrar tabla estructurada en pantalla
        st.dataframe(df_consolidado, use_container_width=True)
        
        # Botón para descargar la base de datos limpia en formato CSV/Excel
        csv_data = df_consolidado.to_csv(index=False).encode('utf-8-sig')
        st.download_button(
            label="📥 Descargar Base de Datos Consolidada (CSV)",
            data=csv_data,
            file_name="consolidado_grupos_maestria.csv",
            mime="text/csv"
        )
        
    # Botón de emergencia para resetear en caso de errores en el salón
    st.subheader("🚨 Control de Datos")
    if st.button("⚠️ Reiniciar toda la base de datos de grupos"):
        db["config_grupos"] = {i: {"departamento": None, "tema": None} for i in range(1, 7)}
        db["estudiantes"] = []
        st.rerun()
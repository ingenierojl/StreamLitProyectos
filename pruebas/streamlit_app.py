import streamlit as st

st.set_page_config(page_title="Mi Página", page_icon="📝") 

# Encabezado
st.header("Mi Página de Ejemplo")

# Barra de navegación 
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="#">Mi Página</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Carrusel
st.markdown("""  
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">

  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="https://picsum.photos/1900/500" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="https://picsum.photos/1900/500?2" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="https://picsum.photos/1900/500?3" alt="Third slide">
    </div>
  </div>
  
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
s
</div>
""", height=400)

# Sección Principal
col1, col2 = st.columns([3,1])

with col1:
   st.header("Bienvenidos") 
   st.write("Contenido principal de la página")
   
with col2:
   st.header("Widget")
   st.write("## Widget sidebar")

# Pie de Página   
st.markdown("""
<nav class="navbar fixed-bottom navbar-dark" style="background-color: #095C63 ;">
  Pie de página
</nav>
""", unsafe_allow_html=True)
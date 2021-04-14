function agregarAutor(){
    const listaAutores = document.getElementById("SeccionAutores");
    const autor = document.createElement("p");

    autor.innerHTML = "<div class=\"form-group\">\n" +
        "   <label for=\"Nombre\">Nombre</label>\n" +
        "   <input type=\"text\" name=\"Nombre[]\" class=\"form-control\" id=\"Nombre\" placeholder=\"escribe el nombre...\">\n" +
        "</div>\n" +
        "<div class=\"form-group\">\n" +
        "   <label for=\"Apellido\">Apellidos del autor</label>\n" +
        "   <input type=\"text\" name=\"Apellido[]\" class=\"form-control\" id=\"Apellido\" placeholder=\"escribe los apellidos...\">\n" +
        "</div>\n" +
        "<div class=\"form-group\">\n" +
        "   <label for=\"Pais\">País del autor</label>\n" +
        "   <input type=\"text\" name=\"Pais[]\" class=\"form-control\" id=\"Pais\" placeholder=\"escribe el país de origen...\">\n" +
        "</div>";

    listaAutores.appendChild(autor);
}

function cargarInfo(infolibro){

    const seccion = document.getElementById("formularioActLibro");
    const parte = document.createElement("p");

    alert("hola")

    parte.innerHTML = "<label>\n" +
        "                        Nombre libro:\n" +
        "                        <input type=\"text\" name=\"Nombre\" class=\"form-control\">\n" +
        "                    </label>"

    seccion.appendChild(parte);

}
import java.io.File

fun leerArchivo(ruta: String): String{
    val archivo = File(ruta) 
    return archivo.readText()
}

fun escribirEnArchivos(ruta: String, content: String){
    val archivo = File(ruta)
    archivo.appendText(content)
}

fun main(args: Array<String>) {
    val ruta = "C:/Users/carlo/OneDrive/Escritorio/ESTRUCTURAS-DE-DATOS/PRACTICAS/PRACTICA6/documentos/archivos.txt"
    val contenido = leerArchivo(ruta)

    /*Ejemplo 1 - lectura de Archivos*/
    println(contenido)
    println("\n")

    /*Ejemplo 2 - Escribir un archivo*/
    val escritura = "\nEsta es una prueba de appendtext."

    escribirEnArchivos(ruta, escritura)
    println("Creado Exitosamente")
}
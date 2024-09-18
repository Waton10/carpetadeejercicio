// principio Solid
/* 
1. Single Responsability Principle (SRP) - Principio de resonsabilidad Unica 
*/

//Ejemplo de no uso de SRP
/*
class factura(val items: List<Item>){
    fun clacularTotal(): Double{
        return items.sumOf {it.precio}
    }
    
    fun generalReporte(): String{
        return "Reporte de la fadtura"
    {
} 
*/

//
class factura(val items: List<Item>){
    fun clacularTotal(): Double{
        return items.sumOf {it.precio}
    }
}    
    
class ReporteFactura {
    fun generar(factura: Factura): String{
        return "Reporte de la factura"
    }
}

/*
2. Open/Clodes Principle (OCP) - Principio Abierto/Cerrado 
*/

open class Empleado(val nombre: String, val horasTrabajados: Int, val precioHora: Double){
    open fun calcularSalario(): Double(
        return horasTrabajadas*precioHora
    )
}

class EmpleadosConBono(nombre: String, horasTrabajadas: Int, precioHora: Double, val bono: Double): Empleado(nombre, horasTrabajadas, precioHora){
    override fun calcularSalario(): Double{
        return super.calcularSalario + bono
    }
}

/*
3. Liskov Subtitution Principle (LSP) - Principio de Sutitucion Liskov 
*/

fun main(args: Array<String>) {
    fun imprimirSalario(empleado: Empleado){
        println("El salario de ${empleado.nombre} es de ${empleado.calcularSalario()}")
    }

    val empleado = Empleado("Daniel", 40, 12.0)
    val EmpleadosConBono = EmpleadosConBono("Fernanda", 40, 12.0, 70.0)

    imprimirSalario(empleado)
    imprimirSalario(EmpleadosConBono)
}

/*
4. Interface Segregation Principle (ISP) - Principio de Segregacion de Intefaces
*/
Interface Trabajado{
    fun trabajar()
}

Inteface Asistente{
    fun asistir()
}

Interface Reportero{
    fun generalReporte()
}

class Programador: Trabajador {
    override fun trabajar(){
        println("El programador esta programando")  
    }
}

class Albanil: Trabajador{
    override fun trabajar(){
        // Agragar de tabajo
    }
}

/*
5. Dependecy Inversion Principle (DIP) - Principio de Inversion de Dependencias
*/

interface Notificaciones{
    fun enviarNotificacion(mensaje: String)
}

class ServicioEmail:Notificaciones{
    override fun enviarNotificacion(mensaje: String){
        println("Enviando Email: $mensaje")
    }
}

class Notificacion(val servicio:Notificaciones){
    fun enviarUnaNotificacion(){
        servicio.enviarNotificacion("Notificacion importante")
    }
}


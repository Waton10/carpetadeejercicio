import kotlin.system.measureTimeMillis

fun main() {
    while (true) {
        println("\nSeleccione una opción:")
        println("1. Ordenar una lista usando Bubble Sort")
        println("2. Ordenar una lista usando Quick Sort")
        println("3. Calcular el factorial de un número")
        println("4. Resolver las Torres de Hanói")
        println("5. Salir")
        print("Opción: ")

        when (readlnOrNull()?.toIntOrNull()) {
            1 -> bubbleSortOption()
            2 -> quickSortOption()
            3 -> factorialOption()
            4 -> hanoiOption()
            5 -> {
                println("Saliendo del programa. ¡Adiós!")
                return
            }
            else -> println("Opción no válida. Inténtelo de nuevo.")
        }
    }
}

fun bubbleSortOption() {
    print("Ingrese una lista de números separados por comas: ")
    val input = readlnOrNull()?.split(",")?.mapNotNull { it.trim().toIntOrNull() }

    if (input.isNullOrEmpty()) {
        println("Entrada no válida. Asegúrese de ingresar números separados por comas.")
        return
    }

    println("Lista original: $input")
    val sortedList: List<Int>
    val executionTime = measureTimeMillis {
        sortedList = bubbleSort(input)
    }
    println("Lista ordenada usando Bubble Sort: $sortedList")
    println("Tiempo de ejecución: ${executionTime / 1000.0} segundos")
}

fun bubbleSort(list: List<Int>): List<Int> {
    val array = list.toMutableList()
    for (i in array.indices) {
        for (j in 0 until array.size - i - 1) {
            if (array[j] > array[j + 1]) {
                val temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            }
        }
    }
    return array
}

fun quickSortOption() {
    print("Ingrese una lista de números separados por comas: ")
    val input = readlnOrNull()?.split(",")?.mapNotNull { it.trim().toIntOrNull() }

    if (input.isNullOrEmpty()) {
        println("Entrada no válida. Asegúrese de ingresar números separados por comas.")
        return
    }

    println("Lista original: $input")
    val sortedList: List<Int>
    val executionTime = measureTimeMillis {
        sortedList = quickSort(input)
    }
    println("Lista ordenada usando Quick Sort: $sortedList")
    println("Tiempo de ejecución: ${executionTime / 1000.0} segundos")
}

fun quickSort(list: List<Int>): List<Int> {
    if (list.size < 2) return list
    val pivot = list[list.size / 2]
    val equal = list.filter { it == pivot }
    val less = list.filter { it < pivot }
    val greater = list.filter { it > pivot }
    return quickSort(less) + equal + quickSort(greater)
}

fun factorialOption() {
    print("Ingrese un número entero positivo: ")
    val input = readlnOrNull()?.toIntOrNull()

    if (input == null || input < 0) {
        println("Entrada no válida. Debe ingresar un número entero positivo.")
        return
    }

    val result = factorial(input)
    println("El factorial de $input es: $result")
}

fun factorial(n: Int): Long {
    return if (n == 0 || n == 1) 1 else n * factorial(n - 1)
}

fun hanoiOption() {
    print("Ingrese el número de discos: ")
    val input = readlnOrNull()?.toIntOrNull()

    if (input == null || input <= 0) {
        println("Entrada no válida. Debe ingresar un número entero positivo mayor a cero.")
        return
    }

    println("Solución para las Torres de Hanói con $input discos:")
    solveHanoi(input, 'A', 'C', 'B')
}

fun solveHanoi(disks: Int, source: Char, target: Char, auxiliary: Char) {
    if (disks == 1) {
        println("Mover disco 1 de Torre $source a Torre $target")
        return
    }
    solveHanoi(disks - 1, source, auxiliary, target)
    println("Mover disco $disks de Torre $source a Torre $target")
    solveHanoi(disks - 1, auxiliary, target, source)
}

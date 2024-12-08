/* Algoritmos de ordenamiento */
import kotlin.system.measureTimeMillis

//bubble sort
fun bubbleSort(arr: IntArray){
    val n = arr.size
    for(i in 0 until n){
        for(j in 0 until n - i - 1){
            if (arr[j] > arr[j + 1]){
                val temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

//Insertion sort
fun insertionSort(arr: IntArray){
    for (i in 1 until arr.size){
        val key = arr[i]
        var j = i - 1
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]
            j -= 1
        }
        arr[j + 1] = key
    }
}

//selection Sort
fun selectionSort(arr: IntArray){
    val n = arr.size
    for (i in 0 until n-1){
        var minIndex = i
        for(j in i + 1 until n){
            if(arr[j] < arr[minIndex]){
                minIndex = j
            }
        }
        val temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp
    }
}

//quick Sort
fun quickSort(arr: IntArray, low: Int, high: Int){
    if  (low < high) {
         val pivot = partition(arr, low, high)
         quickSort(arr, low, pivot - 1)
         quickSort(arr, low + 1, high)
    }
}

fun partition(arr: IntArray, low: Int, high: Int): Int {
    val pivot = arr[high]
    var i = (low - 1)
    for( j in low until high){
        if (arr[j] <= pivot){
            i++
            val temp = arr[i]
            arr[i] = arr[high]
            arr[j] = temp
        }
    }
    val temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp 
    return i+1
}

//merge Sort
fun mergeSort(arr: IntArray){
    if (arr.size < 2) return 
    val middle = arr.size / 2
    var left = arr.copyOfRange(0, middle)
    val right = arr.copyOfRange(middle, arr.size)
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)
}

fun merge(arr: IntArray, left: IntArray, right: IntArray){
    var i = 0
    var j = 0
    var k = 0
    while (i < left.size && j < right.size){
        if(left[i] <= right[j]){
                arr[k++] = left[i++]
            } else {
                arr[k++] = left[j++]
            }
        }
    while (i < left.size) arr[k++] = left[i++]
    while (i < right.size) arr[k++] = left[j++]
}

fun measureSortTime(algorith: (IntArray) -> Unit, arr: IntArray): Long {
    return measureTimeMillis{
        algorith(arr.copyOf())
    }
}

fun main(args: Array<String>) {
    val smallList = (1..10000).toList().shuffled().toIntArray()
    val largeList = (1..100000).toList().shuffled().toIntArray()
    val orderedList = (1..100000).toList().toIntArray()

    println("Tiempos de ejecucion comparativa")

    val bubbleSmall = measureSortTime(::bubbleSort, smallList)
    val insertionSmall = measureSortTime(::insertionSort, smallList)
    val selectionSmall = measureSortTime(::selectionSort, smallList)
    

    println("Bubble sort: $bubbleSmall")
    println("Insetion sort: $insertionSmall")
    println("Selection sort: $selectionSmall")
}
function swap(arr, i, j){
    [arr[i], arr[j]] = [arr[j], arr[i]]
}

function heapFy(arr, lenght, parentIndex){
    let largest = parentIndex
    let left = parentIndex * 2 + 1
    let rigth = left + 1

    if(left < lenght && arr[left] > arr[largest]){
        largest = left
    }
    if(rigth < lenght && arr[rigth] > arr[largest]){
        largest = rigth
    }

    if(parentIndex !== largest){
        swap(arr, parentIndex, largest)
        heapFy(arr, lenght, largest)
    }

    return arr;
}

function heapSort(arr){
    let lenght = arr.length 
    let index = lenght - 1
    let indexParent = Math.floor((index - 1) / 2)

    while(indexParent >= 0){
        heapFy(arr, lenght, indexParent)
        indexParent--
    }
    return arr;
}

console.log(heapSort([5, 7, 8, 3, 4, 2, 6]))
class PQHeap{
    constructor(){
        this.heap = []
    }

    print(){
        if(this.heap.length === 0){
            return false
        }

        for(let index of this.heap){
            console.log(index[0] + ', priority: ' + index[1])
        }
    }

    swap(i, j){
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
    }

    heapFyUp(){
        let index = this.heap.length - 1
        
        while(index > 0){
        let parentIndex = Math.floor((index - 1) / 2)
            if(this.heap[index][1] < this.heap[parentIndex][1]){
                break;
            }

            this.swap(index, parentIndex)
            index = parentIndex
        }
    }

    heapFyDown(){
        let index = 0
        const length = this.heap.length

        while(true){
            let left = Math.floor(index * 2 + 1)
            let rigth = left + 1
            let smallest = index

            if(left < length && this.heap[left] > this.heap[smallest]){
                smallest = left
            }
            if(rigth < length && this.heap[rigth] > this.heap[smallest]){
                smallest = rigth
            }

            if(smallest === index){
                break;
            }

            this.swap(index, smallest)
            index = smallest
        }
    }

    enqueue(elem){
        this.heap.push(elem)
        this.heapFyUp()
    }

    dequeue(){
        if(this.heap.length === 0) return false;
        if(this.heap.length === 1) this.heap.pop();

        const peek = this.heap.pop()
        this.heap[0] = peek
        this.heapFyDown()
        return peek
    }
}

const heap = new PQHeap()

heap.enqueue(['Cauê', 2])
heap.enqueue(['Geovanna', 3])
heap.enqueue(['Alves', 5])
heap.enqueue(['Safira', 7])
heap.enqueue(['Vasconscelos', 1])

heap.print()
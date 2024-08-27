class TaksQueue{
    constructor(){
        this.heap = []
    }

    swap(value1, value2){
        [this.heap[value1], this.heap[value2]] = [this.heap[value2], this.heap[value1]]
    }

    task(){
        if(this.heap.length === 0)return false;

        return 'Task: ', this.heap[0][0]
    }

    enqueue(task){
        this.heap.push(task);
        this.heapFyUp()
    }

    heapFyUp(){
        let index = this.heap.length - 1
        let parentIndex = Math.floor((index - 1) / 2)

        while(index > 0 && this.heap[index][1] > this.heap[parentIndex][1]){
            this.swap(index, parentIndex)
            index = parentIndex
            parentIndex = Math.floor((index - 1) / 2)
        }
    }

    dequeue(){
        if(this.heap.length === 0) return false;
        if(this.heap.length === 1) return this.heap.pop();

        const peek = this.heap[0]
        let last = this.heap.pop()
        this.heap[0] = last
        this.heapFyDown()

        return peek;
    }

    heapFyDown(){
        let index = 0
        let length = this.heap.length

        while(true){
            let left = index * 2 + 1
            let rigth = left + 1
            let largest = index

            if(left < length && this.heap[left][1] > this.heap[largest][1]){
                largest = left
            }
            if(rigth < length && this.heap[rigth][1] > this.heap[largest][1]){
                largest = rigth
            }

            if(largest === index) break;

            this.swap(largest, index)
            index++
        }
    }

    modifyPriority(task, priority){
        const index = this.heap.findIndex(t => t[0] === task)

        if(index === -1) return false;

        

        if(priority > this.heap[index][1]){
            this.heap[index][1] = priority
            this.heapFyUp()
        } else{
            this.heap[index][1] = priority
            this.heapFyDown()
        }
    
    }

}

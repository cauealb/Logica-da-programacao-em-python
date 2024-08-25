class PQ{
    constructor(){
        this.queue = []
    }

    print(){
        if(this.queue.length === 0){
            return false;
        }

        for(let index of this.queue){
            console.log(index[0], ', priority: ', index[1])
        }
    }

    swap(i, j){
        [this.queue[i], this.queue[j]] = [this.queue[j], this.queue[i]]
    }

    heapfyUp(){
        let index = this.queue.length - 1
        let parent = Math.floor((index - 1) / 2)
        
        while(index > 0 && this.queue[index][1] > this.queue[parent][1]){
            this.swap(index, parent)
            index = parent
            parent = Math.floor((index - 1) / 2)
        }
    }

    heapfyDown(){
        let index = 0
        let length = this.queue.length

        while(true){
            let left = index * 2 + 1
            let rigth = left + 1
            let largest = index

            if(left < length && this.queue[left][1] > this.queue[largest][1]){
                largest = left
            }

            if(rigth < length && this.queue[rigth][1] > this.queue[largest][1]){
                largest = rigth
            }

            if(largest === index){
                break;
            }

            this.swap(index, largest)
            index = largest
        }
    }

    enqueue(elem){
        this.queue.push(elem)
        this.heapfyUp()
    }

    dequeue(){
        if(this.queue.length === 0) return false;
        if(this.queue.length === 1) this.queue.pop();

        let peek = this.queue[0]
        let last = this.queue.pop()
        if(this.queue.length > 0){
            this.queue[0] = last
            this.heapfyDown()
        }
    }

    increasePriority(elem){
        const index = this.queue.findIndex(i => i[0] === elem[0])
        
        if(index === -1){
            return false
        }

        if(elem[1] > this.queue[index][1]){
            this.queue[index][1] = elem[1]
            this.heapfyDown()
        }
    }
}

const qp = new PQ()

qp.enqueue(['Cauê', 5])
qp.enqueue(['Geovanna', 2])
qp.enqueue(['Alves', 1])
qp.enqueue(['Vasconscelos', 4])
// Cauê, Vasconcelos, Geovanna, Alves
qp.increasePriority(['Alves', 7])
qp.increasePriority(['Cauê', 6])
qp.increasePriority(['Geovanna', 1])

qp.print()
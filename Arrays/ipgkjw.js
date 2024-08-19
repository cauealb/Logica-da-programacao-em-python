class Queue{
    constructor(){
        this.queue = []
    }

    enqueue(elem){
        this.queue.push(elem)
    }

    dequeue(){
        if(this.isEmpyt()){
            return 'false'
        }
        this.queue.shift()
    }

    peek(){
        if(this.isEmpyt()){
            return 'false'
        }
        
        return this.queue[0]
    }

    size(){
        return this.queue.length
    }

    isEmpyt(){
        return this.queue.length === 0
    }

    print(){
        return this.queue
    }
}

const myQueue = new Queue()

myQueue.enqueue(5)
myQueue.enqueue(17)
myQueue.enqueue(3)
myQueue.enqueue(9)

console.log(myQueue.print())

myQueue.dequeue()

console.log(myQueue.print())

console.log(myQueue.peek())
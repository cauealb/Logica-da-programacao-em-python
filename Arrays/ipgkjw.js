class Node{
    constructor(elem){
        this.elem = elem;
        this.next = null;
    }
};

class Linked{
    constructor(){
        this.length = 0;
        this.head = null;
        this.tail = null
    }

    size(){
        return this.length
    }

    isEmpyt(){
        return this.length === 0
    }

    print(){
        if(this.isEmpyt()){
            return false
        }

        let cur = this.head
        while(cur){
            console.log(cur.elem)
            cur = cur.next
        }
    }

    enqueue(elem){
        const node = new Node(elem)

        if(!this.head){
            this.head = node
            this.length++
            this.tail = node
            return
        }

        this.tail.next = node
        this.tail = node
        this.length++
    }

    dequeue(){
        if(this.isEmpyt()){
            return false
        }

        if(this.length === 1){
            this.head = null;
            this.tail = null;
            this.length--
            return false
        }

        this.head = this.head.next
        this.length--
    }

    peek(){
        if(this.isEmpyt()){
            return false
        }

        return this.head.elem
    }

    cauda(){
        if(this.isEmpyt()){
            return false
        }

        return this.tail.elem
    }
}

class Queue{
    constructor(){
        this.fila = new Linked()
    }

    add(elem){
        return this.fila.enqueue(elem)
    }

    remove(){
        this.fila.dequeue()
    }

    cab(){
        return this.fila.peek()
    }

    top(){
        return this.fila.cauda()
    }

    ver(){
        return this.fila.print()
    }
}

const my = new Queue()

my.add("Cauê")
my.add("Alves")
my.add("Barreto")

my.ver()
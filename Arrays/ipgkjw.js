class Node{
    constructor(elem){
        this.elem = elem;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
        this.length = 0;
        this.tail = null
    }

    add(elem){
        const node = new Node(elem)

        if(!this.head){
            this.head = node
            this.tail = node
            this.length++
            return
        }

        let cur = this.head
        while(cur){
            cur = cur.next
        }

        cur.next = node //O erro começa aqui, corrija!
        this.tail = node
        this.length
    }

    rev(){
        if(this.length === 0){
            return false
        }

        if(this.length === 1){
            this.head = null;
            this.length--
            return
        }

        this.head = this.head.next
        this.length--
    }
}
const MyLinked = new LinkedList()

MyLinked.add(2)
MyLinked.add(5)
MyLinked.add(7)
MyLinked.add(10)
MyLinked.add(515)

MyLinked.rev()
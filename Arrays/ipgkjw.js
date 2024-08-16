class Node{
    constructor(elem){
        this.elem = elem;
        this.next = null
    }
};

class LinkedListSingly{
    constructor(){
        this.head = null;
        this.length = 0
    }

    isEmpyt(){
        return this.length === 0
    }

    size(){
        return this.length
    }

    print(){
        if(this.size() === 0){
            return false;
        }

        let current = this.head
        while(current){
            console.log(current.elem)
            current = current.next
        }
    }

    push(elem){
        const node = new Node(elem)
        if(this.size() === 0){
            this.head = node
            this.length++
            return
        }

        let current = this.head
        while(current.next){
            current = current.next
        }

        current.next = node
        this.length++
    }

    pop(){
        if(this.size() === 0){
            return false
        }

        let current = this.head
        let prev = this.head
        while(current.next){
            prev = current
            current = current.next
        }
        prev.next = null;
    }

    indexAppend(index, elem){
        const node = new Node(elem)

        if(this.size() === 0){
            return false
        }
        if(index > this.length || index < 0){
            return false
        }

        if(index === 0){
            node.next = this.head
            node = this.head
            this.length++
            return
        }

        let current = this.head
        let cont = 1
        while(cont < index){
            current = current.next
            cont++
        }

        current.next = node
        node.next = current.next.next
        this.length++
    }
};

const kiko = new LinkedListSingly()

kiko.push('Cauê')
kiko.push('Alves')
kiko.push('Barreto')

kiko.indexAppend(2, 'Geovanna')
kiko.print()
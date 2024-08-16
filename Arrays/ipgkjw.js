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

        if(index === 1){
            node.next = this.head
            this.head = node
            this.length++
            return
        }

        let current = this.head
        let cont = 1
        while(cont < index){
            current = current.next
            cont++
        }


        if(current.next){
            node.next = current.next
        }
        current.next = node
        this.length++
    }

    removeIndex(index){
        if(this.size() === 0){
            return false
        }
        if(index > this.length || index < 0){
            return false
        }

        if(index === 1){
            this.head = this.head.next
            this.length--
            return
        }

        let current = this.head
        let prev = current
        let cont = 1
        while(cont < index){
            prev = current
            current = current.next
            cont++
        }

        prev.next = null;
        if(current.next){
            prev.next = current.next
        }
        this.length--
    }

    indexSearchElem(index){
        if(this.size() === 0){
            return false
        }
        if(index > this.length || index < 0){
            return false
        }

        let current = this.head
        for(let i = 1; i < index; i++){
            current = current.next
        }

        console.log(current.elem)
    }

    indexSearch(elem){
        if(this.size() === 0){
            return false
        }

        let current = this.head
        let cont = 1
        while(current){
            if(current.elem === elem){
                console.log(cont)
                return
            }else{
                current = current.next
                cont++
            }
        }

        console.log('-1')
    }
};

const kiko = new LinkedListSingly()

kiko.push('Cauê')
kiko.push('Alves')
kiko.push('Barreto')

kiko.indexSearch('Geovanna')
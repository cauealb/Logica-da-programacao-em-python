function myLinkedList(){
    this.length = 0;
    this.head = null;

    function Laco(elem){
        this.elem = elem
        this.next = null
    };

    this.size = function(){
        return this.length
    };

    this.head = function(){
        return this.head
    };


    this.push = function(elem){
        let node = new Laco(elem)
        let currentNode = this.head

        if(this.head === null){
            this.head = node
        }else{
            while(currentNode.next){
                currentNode = currentNode.next
            }
            currentNode.next = node
        }
        this.length++
    }

    this.remove = function(elem){
        let currentNode = this.head
        let anterior;
        if(currentNode.elem === elem){
            currentNode.next = this.head
        }else{
            while(currentNode.elem != elem){
                anterior = currentNode
                currentNode = currentNode.next
            }
            anterior.next = currentNode.next
            currentNode = currentNode.next
        }
        this.length--
    }

    this.void = function(){
        return this.length === 0
    }


    this.serchIndex = function(elem){
        let currentNode = this.head
        let index = -1
        if(index > this.length){
            return false
        }else{
            while(currentNode){
                index++
                if(currentNode.elem === elem){
                    return index
                }else{
                    currentNode = currentNode.next
                }
            }
        }
       return -1 
    }


    this.elemSearch = function(index){
        let currentNode = this.head
        let cont = 0;
        if(index >= this.length){
            return false
        }
        while(cont < index){
            cont++
            currentNode = currentNode.next
        }
        return currentNode.elem
    }


    this.addind = function(index, elem){
        let node = new Laco(elem)
        let currentNode = this.head
        let ponteiro
        let cont = -1

        if(index >= this.length){
            return false
        }
        if(index === 0){
            node.next = currentNode
            this.head = node
        }else{
            while(cont < index){
                cont++
                ponteiro = currentNode
                currentNode = currentNode.next
            }
            node.next = currentNode
            ponteiro.next = node
        }
        this.length++
    }


    this.removeind = function(index){
        let currentNode = this.head
        let pointer
        let cont = -1
        if(index >= this.length){
            return false
        }else{
            if(index === 0){
                this.head = currentNode.next
                pointer = this.head
            }else{
                while(cont < index){
                    cont++
                    pointer = currentNode
                    currentNode = currentNode.next
                }
                pointer.next = currentNode.next
                currentNode = currentNode.next
            }

        }
        this.length-- 
    }

    this.Print = function(){
        let currentNode = this.head
        if(!currentNode){
            return false
        }else{
            while(currentNode){
                console.log(currentNode.elem)
                currentNode = currentNode.next
        }
    }
}

    this.pop = function(){
        let currentNode = this.head
        let pointer

        if(!currentNode){
            return false
        }else{
            if(!currentNode.next){
                return false
            }else{
                while(currentNode.next){
                    pointer = currentNode
                    currentNode = currentNode.next
                }
                pointer.nex = null
                currentNode = null
            }
            this.length--
        }
    }
}

// const list = new myLinkedList()

// list.push('Cauê')
// list.push('Alves')
// list.push('Barreto')

// console.log(list.elemSearch(3))
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Node {
    constructor(elem){
        this.elem = elem;
        this.prev = null;
        this.next = null;
    }
}

class doublyLinkedList{
    constructor(){
        this.head = null
        this.length = 0
    }

    push(elem){
        const node = new Node(elem)

        if(!this.head){
            this.head = node

            this.length++
            return
        }

        let currentNode = this.head
        while(currentNode.next){
            currentNode = currentNode.next
        }

        node.prev = currentNode
        currentNode.next = node
        
        this.length++
        return
    }



    addFirst(elem){
        const node = new Node(elem);
        node.nex = this.head
        if(this.head){
            this.head.prev = node
        }
        this.head = node
        this.length++    
    }

    addLast(elem){
        const node = new Node(elem)
        if(!this.head){
            this.head = node
        }else{
            let currentNode = this.head
            while(currentNode.next){
                currentNode = currentNode.next
            }

            node.prev = currentNode
            currentNode.next = node
        }
        this.length++
    }

    addAt(index, elem){
        if(index < this.length || index > this.length){
            return false
        }
        const node = new Node(elem)
        if(index === 0){
            if(this.head){
                this.head.prev = node
            }
            this.head = node

        }else{
            let currentNode = this.head
            let pointer = null
            for(let i = 0; i < index; i++){
                pointer = currentNode
                currentNode = currentNode.next
            }

            pointer.next = node
            node.prev = pointer
            node.next = currentNode
            if(currentNode){
                currentNode.prev = node
            }
        }
        
        this.length++
    }

    removeFist(){
        if(!this.head){
            return false
        }

        this.head = this.head.next;
        if(this.head){
            this.head = this.head.prev
        }
        this.length--
    }

    removeLast(){
        if(!this.head){
            return false
        }
        if(!this.head.next){
            this.head = null
            this.length--
            return
        }

        let currentNode = this.head
        while(currentNode.next.next){
            currentNode = currentNode.next
        }

        currentNode.next = null
        currentNode.next.prev = null
        this.length--
    }


    removeAt(index){
        if(index > this.length || index < this.length){
            return false
        }

        if(!this.head){
            return false
        }

        let currentNode = this.head
        if(index === 0){
            currentNode.next.prev = null
            if(currentNode,next){
                this.head = currentNode.next
            }
            this.length--
            return
        }

        
        for(let i = 0; i < index; i++){
            lastNode = currentNode
            currentNode = currentNode.next
        }
        let lastNode = currentNode.prev
        let nextNode = currentNode.next

        if(nextNode){
            lastNode.next = nextNode
            nextNode.prev = lastNode   
        }

        currentNode.next = null
        currentNode.prev = null

        this.length-- 

    }


    print(){
        let currentNode = this.head

        while(currentNode){
            console.log(currentNode.elem)
            currentNode = currentNode.next
        }
    }
}

const list = new doublyLinkedList()

list.push('Cauê')
list.push('Alves')


list.print()

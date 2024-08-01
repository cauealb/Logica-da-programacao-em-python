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


function doublyLinkedList(){
    this.length = 0;
    this.head = null;

    function Node(elem, next, last){
        this.elem = elem;
        this.next = null;
        this.last = last;
    }

    this.size = function(){
        return console.log(this.length)
    }

    this.push = function(elem){
        if(!this.head){
            let node = new Node(elem, null, this.head)
        }else{
            let currentNode = this.head
            let last = currentNode
            while(currentNode.next){
                let prev = currentNode
                currentNode = currentNode.next
            }
            let node = new Node(elem, null, last)
        }
        this.length++
    }

    this.print = function(){
        if(this.length === 0){
            return false
        }
        let currentNode = this.head
        while(currentNode){
            console.log(currentNode.elem)
            currentNode = currentNode.nex
        }
    }
}

const list = new doublyLinkedList()

list.push(3)
list.push(5)

list.print()

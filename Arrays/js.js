// class Node{
    // constructor(elem){
    //     this.elem = elem;
    //     this.next = null;
    //     this.prev = null;
    // }

// }

// class linked{
//     constructor(){
//         this.length = 0
//         this.head = null
//     }

//     print(){
//         if(!this.head){
//             return false
//         }

//         let currentNode = this.head
//         while(currentNode){
//             console.log(currentNode.elem)
//             currentNode = currentNode.next
//         }
//     }


//     push(elem){
//         const node = new Node(elem)

//         if(!this.head){
//             this.head = node
//             this.length++
//             return
//         }

//         let currentNode = this.head
//         while(currentNode.next){
//             currentNode = currentNode.next
//         }
//         node.prev = currentNode
//         currentNode.next = node

//         this.length++
//     }

//     pop(){
//         if(!this.head){
//             return false
//         }

//         let currentNode = this.head
//         let previus
//         while(currentNode.next){
//             previus = currentNode
//             currentNode = currentNode.next
//         }
//         currentNode.prev = null
//         previus.next = null

//         this.length--
//     }
    
//     append(index, elem){
//         const node = new Node(elem)
//         // if(index < this.length || index >= this.length){
//         //     return false
//         // }
//         if(!this.head){
//             this.head = node
//             this.length++
//             return
//         }
//         if(index === 0){
//             this.head.prev = node
//             node.next = this.head
//             this.head = node
//             this.length++
//             return true
//         }

//         let currentNode = this.head
//         let previus
//         for(let i = 0; i < index; i++){
//             previus = currentNode
//             currentNode = currentNode.next
//         }

//         previus.next = node
//         node.prev = previus

//         if(currentNode){
//             currentNode.prev = node
//             node.next = currentNode
//         }

//         this.length++
//         return true

//     }

//     trash(index){
//         if(!this.head){
//             return false
//         }
//         if(index === 0){
//             this.head.next.prev = null;
//             this.head.nex = this.head
//             this.length--
//             return
//         }

//         let currentNode = this.head 
//         let previus
//         let nextNode
//         for(let i = 0; i < index; i++){
//             previus = currentNode
//             currentNode = currentNode.next
//         }
//         nextNode =currentNode.next

//         previus.next = nextNode
//         nextNode.prev = previus

//         this.length--

//     }

// }


class Node{
    constructor(elem){
        this.elem = elem;
        this.next = null;
    }
}

class linked{
    constructor(){
        this.length = 0;
        this.head = null;
    };

    print(){
        if(!this.head){
            return false
        }

        let currentNode = this.head
        while(currentNode){
            console.log(currentNode.elem)
            currentNode = currentNode.next
        }
    };

    push(elem){
        const node = new Node(elem)

        if(!this.head){
            this.head = node
            this.length++
            return
        }else{
            let currentNode = this.head
            while(currentNode.next){
                currentNode = currentNode.next
            }
            currentNode.next = node
        }
        this.length++
    };

    pop(){
        if(!this.head){
            return false
        }
        if(!this.head.next){
            this.head = null
            this.length--
            return 
        }

        let currentNode = this.head
        let previus
        while(currentNode.next){
            previus = currentNode
            currentNode = currentNode.next
        }

        previus.next = null
        this.length--
    }

    pushMidIndex(index, elem){
        const node = new Node(elem)

        if(index < 0 || index > this.length){
            return false
        }
        if(!this.head.next){
            this.head = null
            this.length--
            return
        }

        let currentNode = this.head
        let previus
        for(let i = 0; i < index; i++){
            previus = currentNode
            currentNode = currentNode.next
        }

        if(currentNode.next){
            previus.next = node
            node.next = currentNode
        }
        this.length--
    }

    popMidIndex(index){
        if(index < 0 || index > this.length){
            return false
        }
        if(index === 0){
            this.head.next = this.head
            this.length--
        }

            let currentNode = this.head
            let previus
            for(let i = 0; i < index; i++){
                previus = currentNode
                currentNode = currentNode.next
            }

            if(currentNode.next){
                previus.next = currentNode.next
            }
            currentNode = null
            this.length--
        }


        indexOf(index){
            if(index < 0 || index >= this.length){
                return -1
            }

            let currentNode = this.head
            for(let i = 0; i < index; i++){
                currentNode = currentNode.next
            }
            
            return currentNode.elem
        }

        removeElems(elem){
            if(!this.head){
                return false
            }
            

            let currentNode = this.head
            let previus
            while(currentNode){

                if(currentNode.elem === elem){
                    previus.next = currentNode.next
                    currentNode = currentNode.next

                }else{
                    previus = currentNode
                    currentNode = currentNode.next
                }

            }
            return true
    }
}


const list = new linked()

list.push(1)
list.push(2)
list.push(6)
list.push(3)
list.push(4)
list.push(5)
list.push(6)

var hasCycle = function(head) {

    let current = head
    let array = new Array()

    while(current){
        array.push(current.val)
    }

    

};

hasCycle(1)




function linkedList(){
    this.lenght = 0;
    this.head = null;


    const Node = function(elem){
        this.elem = elem;
        this.next = null;
    }

    this.size = function(){
        return length
    }

    this.head = function(){
        return head
    }

    this.add = function(){

        let node = new Node(elem)
        if(head === null){
            head = node
        }else{
            let currentNode = head
            while(currentNode.next){
                currentNode = currentNode.next
            }
            currentNode = node
        }
        
        lenght++
    }


    this.remove = function(elem){

        let currentNode = head
        let previusNode;
        if(currentNode.elem === elem){
            currentNode.next = head
        }else{
            while(currentNode.elem != elem){
                previusNode = currentNode
                currentNode = currentNode.next
            }
            previusNode.next = currentNode.next

        }
        lenght--
    }

    this.isEmpty = function(){
        return lenght === 0
    };

    this.indexOf = function(elem){
        let currentNode = head;
        let index = -1;

        while(currentNode){
            index++
            if(currentNode.elem === elem){
                return index;
            }else{
                currentNode = currentNode.next
            }
            
        }
        return -1;
    };

    this.ElemIndex = function(value){
        let currentNode = head
        let cont = -1

        while(cont < value){
            cont++
            currentNode = currentNode.next
        }
        return currentNode.elem
    };


}
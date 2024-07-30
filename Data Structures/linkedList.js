
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
            while(currentNode.next != elem){
                previusNode = currentNode.elem
                currentNode = currentNode.next
            }
            
            
        }
    }



}


linkedList.elem(e)
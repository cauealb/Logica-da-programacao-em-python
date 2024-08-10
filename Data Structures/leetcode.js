class Node{
    constructor(elem){
        this.elem = elem;
        this.next = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
        this.top = this.head
        this.lenght = 0;
    }

    add(elem){
        const node = new Node(elem)

        if(!this.head){
            this.head = node
            this.lenght++
        }else{

            let current = this.head
            while(current.next){
                current = current.next
            }
    
            current.next = node
            this.top = node
        }
        this.lenght++
    }

        

    remove(){
        if(this.lenght === 0){
            return 'This List is Empty'
        }

        if(this.lenght === 1){
            this.head = null
            this.lenght--
        }else{
            let current = this.head
            let prev = current
            while(current.next){
                prev = current
                current = current.next
            }
            prev.next = null
            this.top = prev
        
        }
        this.lenght--
    }

    peekTop(){
        if(this.lenght === 0){
            return 'This List is Empty'
        }

        let current = this.head
        while(current.next){
            current = current.next
        }

        return current.elem
    }


    ver(){
        if(this.lenght === 0){
            return 'This List is Empty'
        }

        let current = this.head
        while(current){
            console.log(current.elem)
            current = current.next
        }
    }
}

class Stack{
    constructor(){
        this.Stack = new LinkedList()
        this.top = null;
    }

    size(){
        return this.Stack.lenght
    }

    push(elem){
        return this.Stack.add(elem)
    }

    pop(){
        if(this.size() === 0){
            return 'This stack is Empyt'
        }

        return this.Stack.remove()
    }

    peek(){
        if(this.size() === 0){
            return 'This stack is Empyt'
        }

        return this.Stack.peekTop()
    }

    print(){
        this.Stack.ver()
    }

}


const nn = new Stack()

nn.push(10)
nn.push(20)
nn.push(30)
nn.push(40)

nn.pop()
nn.print()

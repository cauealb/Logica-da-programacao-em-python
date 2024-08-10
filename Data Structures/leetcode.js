class Stack{
    constructor(){
        this.stack = []
    }

    size(){
        return this.stack.length
    }

    isEmpyt(){
        return this.size() === 0
    }

    push(elem){
        return this.stack.push(elem)
    }

    pop(){
        if(this.isEmpyt()){
            return 'This Stack is Empty'
        }

        return this.stack.pop()
    }

    peek(){
        if(this.isEmpyt()){
            return 'This Stack is Empty'
        }

        return this.stack[this.size() - 1]
    }
}
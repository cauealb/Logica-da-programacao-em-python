class Stack {
    constructor(){
        this.stack = []
    }

    IsEmpty(){
        return size() === 0
    }

    push(elem){
        this.stack.push(elem)
    }

    pop(){
        if(this.IsEmpty()){
            return false
        }

        return this.stack.pop()
    }

    peek(){
        if(this.IsEmpty()){
            return false
        }

        return this.stack[size() - 1]
    }

    size(){
        return this.stack.length
    }
}
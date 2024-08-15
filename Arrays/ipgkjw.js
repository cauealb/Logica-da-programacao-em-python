
class Stack{
    constructor() {
        this.Stack = []
    }

    push(elem){
        this.Stack.push(elem)
    };

    pop(){
        return this.Stack.pop()
    }

    peek(){
        return this.Stack[this.Stack.length - 1]
    }

    size(){
        return this.Stack.length
    }

    isEmpyt(){
        return this.Stack.length === 0
    }

}

const list = new Stack()

list.push('Cauê')
list.push('Alves')
list.push('Barreto')

console.log(list.isEmpyt())
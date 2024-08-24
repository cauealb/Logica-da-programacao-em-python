class PQ{
    constructor(){
        this.pq = []
    }

    print(){
        console.log(this.pq)
    }

    dequeue(){
        return this.pq.shift()
    }

    enqueue(elem){
        if(this.pq.length === 0){
            this.pq.push(elem)
            return
        }
        let cont = false
        for(let i = 0; i < this.pq.length; i++){
            if(elem[1] < this.pq[i][1]){
                this.pq.splice(i, 0, elem)
                cont = true
                break
            }
        }

        if(!cont){
            this.pq.push(elem)
        }
    }
}

const pq = new PQ()

pq.enqueue(['Alves', 2])
pq.enqueue(['Cauê', 1])
pq.enqueue(['Vasconcelos', 4])
pq.enqueue(['Geovanna', 3])


pq.print()
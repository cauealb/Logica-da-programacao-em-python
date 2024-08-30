class Uniao{
    constructor(size){
        this.arr = new Array(size).fill(1).map((_, index) => index)
        this.rank = new Array(size).fill(1)
    }

    find(x){
        if(this.arr[x] !== x){
            this.arr[x] = this.find(this.arr[x])
        }
        return this.arr[x]
    }

    union(x, y){
        const raizX = this.find(x)
        const raizY = this.find(y)

        if(raizX !== raizY){
            if(this.rank[raizX] > this.rank[raizY]){
                this.arr[raizY] = raizX
            } else if(this.rank[raizX] < this.rank[raizY]){
                this.arr[raizX] = raizY
            }else{
                this.arr[raizY] = raizX
                this.rank[raizX] += 1
            }
        }
    }

    connected(x, y){
        return this.find(x) === this.find(y)
    }
}

const uu = new Uniao(11)

uu.union(1, 5)
uu.union(5, 10);

console.log(uu.find(10))
// // // // // class Node{
// // // // //     constructor(elem){
// // // // //         this.elem = elem;
// // // // //         this.next = null;
// // // // //     }
// // // // // }

// // // // // class SiglyLinded{
// // // // //     constructor(){
// // // // //         this.length = 0;
// // // // //         this.head = null;
// // // // //         this.tail = null;
// // // // //     }

// // // // //     size(){
// // // // //         return this.length
// // // // //     }

// // // // //     isEmpty(){
// // // // //         return this.length === 0
// // // // //     }

// // // // //     push(elem){
// // // // //         const node = new Node(elem)

// // // // //         if(this.isEmpty()){
// // // // //             this.head = node
// // // // //             this.tail = node
// // // // //             this.length++
// // // // //             return
// // // // //         }

// // // // //         this.tail.next = node
// // // // //         this.tail = node
// // // // //         this.length++
// // // // //     }

// // // // //     pop(){
// // // // //         if(this.isEmpty()){
// // // // //             return false;
// // // // //         }

// // // // //         if(this.size() === 1){
// // // // //             this.head = null;
// // // // //             this.length--
// // // // //             return 
// // // // //         }

// // // // //         this.head = this.head.next
// // // // //         this.length--
// // // // //     }

// // // // //     middlePush(index, elem){
// // // // //         if(index > this.length && index < 0){
// // // // //             return false;
// // // // //         }
        
// // // // //         const node = new Node(elem)
// // // // //         let cur = this.head
// // // // //         for(let i = 0; i < index; i++){
// // // // //             cur = cur.next
// // // // //         }

// // // // //         node.next = cur.next
// // // // //         cur.next = node
// // // // //         this.length++
// // // // //     }

// // // // //     middlePop(index){
// // // // //         if(index > this.length && index < 0){
// // // // //             return false;
// // // // //         }

// // // // //         let cur = this.head
// // // // //         let prev = cur
// // // // //         for(let i = 0; i < index; i++){
// // // // //             prev = cur
// // // // //             cur = cur.next
// // // // //         }

// // // // //         prev.next = cur.next
// // // // //         this.length--
// // // // //     }
// // // // // }

// // // // class Node{
// // // //     constructor(elem){
// // // //         this.elem = elem
// // // //         this.next = this.next
// // // //         this.prev = this.prev
// // // //     }
// // // // }

// // // // class Doubly{
// // // //     constructor(){
// // // //         this.length = 0;
// // // //         this.head = null;
// // // //         this.tail = null;
// // // //     }

// // // //     print(){
// // // //         if(this.isEmpty()){
// // // //             return false;
// // // //         }

// // // //         let cur = this.head
// // // //         while(cur){
// // // //             console.log(cur.elem)
// // // //             cur = cur.next
// // // //         }
// // // //     }

// // // //     size(){
// // // //         return this.length
// // // //     }
        
// // // //     isEmpty(){
// // // //         return this.length === 0
// // // //     }

// // // //     push(elem){
// // // //         const node = new Node(elem)

// // // //         if(this.isEmpty()){
// // // //             this.head = node
// // // //             this.tail = node
// // // //             this.length++
// // // //             return
// // // //         }

// // // //         this.tail.next = node
// // // //         node.prev = this.tail
// // // //         this.tail = node
// // // //         this.length++
// // // //     }

// // // //     pop(){
// // // //         if(this.isEmpty()){
// // // //             return false
// // // //         }

// // // //         if(this.size() === 1){
// // // //             this.head = null;
// // // //             return
// // // //         }

// // // //         let cur = this.head
// // // //         let ant = cur
// // // //         while(cur.next){
// // // //             ant = cur
// // // //             cur = cur.next
// // // //         }

// // // //         ant.next = null;
// // // //         this.tail = ant
// // // //         this.length--
// // // //     }

// // // //     middlePush(index, elem){
// // // //         if(index > this.length && index < 0){
// // // //             return false;
// // // //         }
// // // //         const node = new Node(elem)

// // // //         let cur = this.head
// // // //         let ant = cur
// // // //         for(let i = 0; i < index; i++){
// // // //             ant = cur.next.next
// // // //             cur = cur.next
// // // //         }

// // // //         cur.next = node
// // // //         node.next = ant
// // // //     }

// // // //     middlePop(index){
// // // //         if(index > this.length && index < 0){
// // // //             return false;
// // // //         }

// // // //         let cur = this.head
// // // //         let ant = cur
// // // //         for(let i = 0; i < index; i++){
// // // //             ant = cur
// // // //             cur = cur.next
// // // //         }

// // // //         ant.next = cur.next
// // // //         cur.next.prev = ant

// // // //     }
// // // // }
// // // // const Linek = new Doubly()

// // // // Linek.push('Cauê')
// // // // Linek.push('Alves')
// // // // Linek.push('Barreto')

// // // // Linek.middlePop(1)

// // // // Linek.print()

// // // class Stack{
// // //     constructor() {
// // //         this.Stack = []
// // //     }

// // //     isEmpty(){
// // //         return this.Stack.length === 0
// // //     }

// // //     size(){
// // //         return this.Stack.length
// // //     }

// // //     push(elem){
// // //         return this.Stack.push(elem)
// // //     }

// // //     pop(){
// // //         if(this.isEmpty()){
// // //             return false;
// // //         }

// // //         return this.Stack.pop()
// // //     }

// // //     peek(){
// // //         return this.Stack[this.Stack.length - 1]
// // //     }
// // // }

// // // const pilha = new Stack()

// // // pilha.push('Cauê')
// // // pilha.push('Alves')
// // // pilha.push('Barreto')

// // // pilha.pop()
// // // console.log(pilha.size())

// // class PQueue{
// //     constructor(){
// //         this.queue = []
// //     }

// //     print(){
// //         console.log(this.queue)
// //     }

// //     peek(){
// //         return this.queue[0][0]
// //     }

// //     pop(){
// //         return this.queue.shift()
// //     }

// //     push(elem){
// //         let cont = false
// //         for(let i = 0; i < this.queue.length; i++){
// //             if(elem[1] > this.queue[i][1]){
// //                 this.queue.splice(i, 0, elem)
// //                 cont = true
// //                 break;
// //             }
// //         }

// //         if(!cont){
// //             this.queue.push(elem)
// //         }
// //     }
// // }

// // const pq = new PQueue()

// // pq.push(['Cauê', 3])
// // pq.push(['Geovanna', 1])
// // pq.push(['Alves', 10])

// // pq.pop()
// // console.log(pq.peek())

// class Heap{
//     constructor() {
//         this.Heap = []
//     }

//     print(){
//         return this.Heap
//     }

//     swap(x , y){
//         [this.Heap[x], this.Heap[y]] = [this.Heap[y], this.Heap[x]]
//     }

//     peek(){
//         return this.Heap[0]
//     }

//     push(elem){
//         this.Heap.push(elem)
//         this.HeapFyUp()
//     }

//     HeapFyUp(){
//         let index = this.Heap.length - 1
//         let indexParent = Math.floor((index - 1) / 2)

//         while(index > 0 && this.Heap[index] > this.Heap[indexParent]){
//             this.swap(index, indexParent)
//             index = indexParent
//             indexParent = Math.floor((index - 1) / 2)
//         }
//     }

//     HeapFyDown(){
//         let index = 0

//         while(true){
//             let left = index * 2 + 1
//             let rigth = left + 1
//             let largest = index

//             if(left > 0 && this.Heap[left] > this.Heap[largest]){
//                 largest = left
//             }
//             if(rigth > 0 && this.Heap[rigth] > this.Heap[largest]){
//                 largest = rigth
//             }

//             if(largest === index){
//                 break;
//             }

//             this.swap(largest, index)
//             index++
//         }

//     } 

//     pop(){
//         if(this.Heap.length === 0) return false;
//         if(this.Heap.length === 1) return this.Heap.pop();

//         const peek = this.Heap[0]
//         let last = this.Heap.pop()
//         this.Heap[0] = last
//         this.HeapFyDown()

//         return peek

//     }
// }

// const pq = new Heap()

// pq.push(1)
// pq.push(5)
// pq.push(3)
// pq.push(7)

// pq.pop()
// console.log(pq.print())
// //Console
// console.log("Olá JavaScript")
// console.error("Error")
// console.warn("Aviso!!")
//========================================================================


//Variáveis
// var x = 5
// let y = 10
// const z = 20

// if(false){
//     y = 6
// }

// console.log(x)
// console.log(y)
// console.log(z)

// let name = 'Cauê'
// console.log(typeof name)

// let num = 30.6
// console.log(typeof num)

// let aprovado = true
// console.log(typeof aprovado)

// let nada = null;
// if(typeof nada === 'object'){
//     console.log('0i')
// }

// let age
// console.log(typeof age)

// const arr = ['JS', 'Java', 'Python']
// console.log(arr)
// console.log(typeof arr)

// const user = {name: 'Cauê', age: 18, height: null}
// console.log(user)
// console.log(typeof user)
//=================================================================

//Métodos de String
// let name = 'Cauê Alves'

// console.log(name.toLowerCase())
// console.log(name.toUpperCase())
// console.log(name.slice(0, 5))
//========================================================================================

//Métodos de Array

// const lin = ['Javascript', 'Python', 'Java', 'CSharp']

// console.log(lin.length)

// lin.unshift('Node')
// console.log(lin)
//==========================================================================================

//Objetos

// const Product = {
//     name: 'Mouse',
//     larg: 12.0,
//     colors: ['White', 'Black', 'Yellow'],
//     inStock: false,
// }

// console.log(Product.colors)

// console.log(Product['larg'])

// //Destructuring

// const {name, inStock} = Product 

// console.log(name)
// console.log(inStock)

// const [lin1 , lin2] = lin

// console.log(lin1)
// console.log(lin2)

//======================================================

//JSON - Javascript Object Notation

// const jj = {
//     name: 'Camisa',
//     prince: 15.99
// }

// const Jason = JSON.stringify(jj)

// console.log(Jason)

// const obj = JSON.parse(Jason)

// console.log(Jason)
//==============================================================

//Estruturas condicionais

// let num = 90

// let resp = num < 100 ? true : false

// console.log(resp)
//===============================================================

//Métodos de array -> repetição

// const lin = ['Javascript', 'HTML', 'CSS', 'CSharp']

// lin.forEach(function(names){
//     console.log(names)
// })

// const mod = lin.map(function(name){
//     if(name === 'HTML'){
//         return (name = 'Node');
//     }else if(name === 'CSS'){
//         return (name = 'React');
//     }else{
//         return name;
//     } 
// })

// console.log(mod)

// const minNumber = [50, 6, 89, 34, 8, 12, 77, 34].filter(function(number){
//     return number < 25
// })

// console.log(minNumber)

// const sumAll = [10, 20, 30, 40, 50].reduce(function(total, number){
//     return total += number
// })

// console.log(sumAll)


const arr = ['Youtube', 'Instagram', 'Facebook', 'Tiktok']

// const nome = arr.forEach(function(bigT){
//     console.log(bigT)
// })


// const NewArr = arr.map(function(big){
//     if(big === 'Facebook'){
//         return (big = 'WhatsApp')
//     }else{
//         return big;
//     }
// })

// console.log(NewArr)
//===============================================================

//Funções 

// function imprimirNome(fNome, lNome){
//     return `Olá ${fNome} ${lNome}`
// }

// let firstName = 'Cauê'
// let lastName = 'Alves'

// console.log(imprimirNome(firstName, lastName))
//==============================================================

//Arrow Functions

// const ife = 5 < 10 ? true : false
// console.log(ife)
// const myFunction = (a, b) => a + b

// console.log(myFunction(5, 6))
//===============================================================

//Classes

// class Product{
//     constructor(prince, size){
//         this.prince = prince
//         this.size = size
//     }

//     showProduct(prince, size){
//         return `O Mouse tem um preço de ${this.prince}`
//     }
// }
 
// class SuperProduct extends Product{
//     constructor(prince, size, name){
//         super(prince, size)
//         this.name = name
//     }

//     mostrar(name, prince, size){
//         return `O ${this.name} tem um preço de ${this.prince} e um tamanho de ${this.size}`
//     }

//     static valiar(){
//         return `Estamos funcionando`
//     }
// }

// const prod = new SuperProduct(12, 10, 'Compiuter')

// console.log(prod.mostrar('Compiuter', 14 , 34))

// console.log(SuperProduct.valiar())
//=================================================================================

// DOM - Document Object Model

// const title = document.getElementById('title')

// console.log(title)

// const id = document.querySelector('#title')

// console.log(id)

// const peg = document.querySelectorAll('.text')

// console.log(peg)
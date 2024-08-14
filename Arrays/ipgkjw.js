// var clearDigits = function(s) {
//     const splitA = s.split('');
//     let array = [];
//     let j, number, cont = -1;

//     for(let i of splitA){
//         number = Number(i);
//         if(number >= 0){
//             array.push(number);
//         }else{
//             array.push(i);
//         }
//     }

//     for(let i of array){
//         cont++;
//         j = cont - 1;
//         if(typeof i === 'number'){ 
//             array.splice(cont, 1);
//             array.splice(j, 1);
//         }
//     }
//     return array;
// };




const clearElem = function(s){
    const splitA = s.split('');
    let array = [];
    let number;

    for(let i of splitA){
        number = Number(i)
        if(i >= 0){
            array.pop()
        }else{
            array.push(i)
        }
    }
    let answer = array.join('').trim()
    return answer;
}

clearElem('abc')
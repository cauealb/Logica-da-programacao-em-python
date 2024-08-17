const removeStars = function(s){
    const separa = s.split('')
    let array = []

    for(let i of separa){
        if(i !== '*'){
            array.push(i)
        }else{
            array.pop()
        }
    }

}

removeStars('leet**cod*e')
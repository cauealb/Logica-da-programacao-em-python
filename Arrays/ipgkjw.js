
let ds = [1, 2, 2, 4]
let dr = []
let cont
while(ds){
    dr.unshift(ds[cont])
}


let contrario = ds.join('')
let certo = dr.join('')

if(contrario === certo){
    return true;
}else{
    return false;
}
function ListNode(val, next) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
}


const linked = function(head){
    if(!head){
        return false
    }
    let current = head
    let cont = 0

    while(current){
        current = current.next
        cont++
    }

    let middle = cont / 2
    let currentNew = head

    for(let i = 0; i < middle; i++){
        currentNew = current.next
    }

    return 

}
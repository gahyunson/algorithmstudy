# Linked List Structure
order collection of the data  
has chain  
always two special node - Head node , Tail node  
Node = Data + Reference to Next Node  

```javascript
const nodeOne = {
    data: 123
};

const nodeTwo = {
    data: 456
};

nodeOne.next = nodeTwo;

```
if don't have reference any other node -> it is tail

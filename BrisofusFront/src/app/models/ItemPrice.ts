import Item from "./Item";

export default class ItemPrice{
    id:number;
    price:number;
    item:Item;
    date:Date;
    hdvPrice:number;
    constructor(){  
        this.id=0;
        this.hdvPrice=0;
        this.price=0;
        this.item=new Item();
        this.date=new Date();
    }
}
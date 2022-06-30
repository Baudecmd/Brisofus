import Item from "./Item";

export default class HistoricPrice{
    price:number;
    item:Item;
    d:Date;
    constructor(){  
        this.price=0;
        this.item=new Item();
        this.d=new Date();
    }
}
import Item from "./Item";

export default class HistoricComparePrice{
    item:Item;
    price:number;
    averagePrice:number;
    ratio:number;

    constructor(){
        this.item=new Item();
        this.price=0;
        this.averagePrice=0;
        this.ratio=0;
    }
}

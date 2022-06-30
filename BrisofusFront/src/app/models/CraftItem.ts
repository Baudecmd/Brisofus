import Item from "./Item";

export default class CraftItem{
    resourceItem:Item;
    quantite:number;
    id:number;

    constructor(){
        this.resourceItem=new Item();
        this.quantite=0;
        this.id=0;
    }

    getTotalPrice():number{
        return this.quantite*this.resourceItem.lastPrice;
    }

}
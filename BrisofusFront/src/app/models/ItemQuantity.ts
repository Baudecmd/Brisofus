import Item from "./Item";

export default class ItemQuantity{
    resourceItem:Item;
    quantite:number;

    constructor(){
        this.resourceItem=new Item();
        this.quantite=0;
    }


}
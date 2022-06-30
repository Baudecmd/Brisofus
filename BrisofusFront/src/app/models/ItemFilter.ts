export default class ItemFilter{
    listAttribute:String[];
    listType:String[];
    levelMin:number;
    levelMax:number;
    searchName:String;

    constructor(){
        this.listAttribute=[];
        this.listType=[];
        this.levelMax=60;
        this.levelMin=40;
        this.searchName=""
    }

    removeListAttribute(attribute:String){
        this.listAttribute = this.listAttribute.filter(obj => obj !== attribute);
    }
}
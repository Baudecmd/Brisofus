import HistoricPrice from "./HistoricPrice";

export default class HistoricPriceGraph{
    label:string;
    historicPrices:HistoricPrice[];

    constructor(label:string,historicPrices:HistoricPrice[]){
        this.label="";
        this.historicPrices=[];
    }
}

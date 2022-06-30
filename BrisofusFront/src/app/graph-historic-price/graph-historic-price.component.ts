import { Component, Input, OnInit } from '@angular/core';
import HistoricPrice from '../models/HistoricPrice';
import HistoricPriceGraph from '../models/HistoricPriceGraph';

@Component({
  selector: 'app-graph-historic-price',
  templateUrl: './graph-historic-price.component.html',
  styleUrls: ['./graph-historic-price.component.css']
})
export class GraphHistoricPriceComponent implements OnInit {
  listOfPrice: any[] = [];

  @Input()
  label:string="";
  @Input()
  historicPrices: HistoricPriceGraph[] = [];

  constructor() { }

  ngOnInit(): void {
    this.historicPrices.forEach((elem) => {
      this.listOfPrice.push(
        {
          series: elem.historicPrices.map(element => { return { name: element.d.toLocaleString().substring(0, 10), value: element.price }; }),
          name: elem.label
        }
      )
    }
    );

  }

}

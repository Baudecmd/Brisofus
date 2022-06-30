import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HistoricPriceServiceService } from '../historic-price-service.service';
import HistoricPrice from '../models/HistoricPrice';
import Item from '../models/Item';
import { ItemService } from '../services/item.service';
import { Location } from '@angular/common';
import HistoricPriceGraph from '../models/HistoricPriceGraph';

@Component({
  selector: 'app-item-details',
  templateUrl: './item-details.component.html',
  styleUrls: ['./item-details.component.css']
})

export class ItemDetailsComponent implements OnInit {
  itemName: String = "";
  item: Item = new Item();
  historicPrices: HistoricPrice[] = [];
  listOfPrice: any[] = [];
  historicPricesHDV: HistoricPriceGraph[] = [];



  constructor(private location: Location,private route: ActivatedRoute, private itemService: ItemService, private historicSerivce: HistoricPriceServiceService) {
    this.route.params.subscribe(params => { this.itemName = params['name']; });
  }

  ngOnInit(): void {
    this.itemService.getItemDetails(this.itemName).subscribe(itemDetail => {
      this.item = itemDetail;

    });

    this.historicSerivce.getHistoricPrice(this.itemName).subscribe(historicPrices => {
      console.log(historicPrices);
      this.historicPrices = historicPrices
      this.listOfPrice = [
        {
          series: this.historicPrices.map(element => {return {name:element.d.toLocaleString().substring(0,10),value:element.price};}),
          name: 'Prix de craft'
        }
      ];
    });


    this.historicSerivce.getHistoricPriceHDV(this.itemName).subscribe((elem)=>{
        this.historicPricesHDV.push(new HistoricPriceGraph("Prix de vente",elem));
    });
  }


  back(): void {
    this.location.back()
  }

}

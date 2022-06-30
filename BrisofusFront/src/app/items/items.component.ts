import { Component, Input, OnInit } from '@angular/core';
import { ItemService } from '../services/item.service';
import { Router } from '@angular/router';
import { SearchItemService } from '../search-item.service';
import { BreakingsService } from '../breakings.service';
@Component({
  selector: 'app-items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.css']
})
export class ItemsComponent implements OnInit {

  loading:boolean=false;

  addOnBlur = true;

  list_type=
  ["Bottes","Ceinture","Chapeau","Cape","Anneau","Amulette","Baguette","Bâton"];

stat_list=[
    "% Critique",
    "Vitalité",
    "Agilité",
    "Sagesse",
    "Chance",
    "Fuite",
    "Force",
    "Tacle",
    "Intelligence",
    "Prospection",
    "Portée",
    "Dommages Feu",
    "Dommages Eau",
    "Dommages Air",
    "Dommages Terre",
    "% Résistance Feu",
    "% Résistance Eau",
    "% Résistance Air",
    "% Résistance Terre",
    "Retrait PM",
    "Retrait PA",
    "PM",
    "PA"
  ];

  constructor(public breakingService:BreakingsService,private itemService:ItemService,private router: Router,public searchService:SearchItemService) { }



  ngOnInit(): void {
    this.loading=false;
    this.searchItem();
    this.searchService.itemFilter.listType=this.list_type;
  }

  counter(i: number) {
    return new Array(i);
}
  
  searchItem(){
    this.loading=true;
    this.itemService.searchItemPrice(this.searchService.itemFilter).subscribe(value => {
      this.loading=false;
      console.log(value);
      this.searchService.itemPriceList=value;
      this.searchService.itemPriceList=this.searchService.itemPriceList.filter((elem)=>elem!=null);
    })

  }

  onClick(name:String) {
    this.router.navigate(['item', name]);
  }


}

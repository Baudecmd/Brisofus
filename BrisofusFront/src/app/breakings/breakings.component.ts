import { Component, OnInit } from '@angular/core';
import { BreakingsService } from '../breakings.service';

@Component({
  selector: 'app-breakings',
  templateUrl: './breakings.component.html',
  styleUrls: ['./breakings.component.css']
})
export class BreakingsComponent implements OnInit {

  constructor(public breakingService:BreakingsService) { }

  ngOnInit(): void {
  }

  breakingBotButton(){
    this.breakingService.brisageItem().subscribe((val: any)=>{
      console.log(val);
    })
  }

}

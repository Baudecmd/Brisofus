import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-appbar',
  templateUrl: './appbar.component.html',
  styleUrls: ['./appbar.component.css']
})
export class AppbarComponent implements OnInit {
  items: MenuItem[]=[];
  constructor() { 
    
  }

  ngOnInit() {
    this.items = [
        {
            label: 'Suiveur de prix',
            items: [{
                    label: 'Ressources', 
                    routerLink: ['/items']
                },
                {label: 'Équipement',routerLink: ['/items']}
            ]
        },
        {
            label: 'Brisages',
            items: [{
                    label: 'Mes objets', 
                    routerLink: ['/breakings']
                }
            ]
        },
    ];
}

}

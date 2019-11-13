import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'PIM-front';
  categories ;
  subcategories;
  cars = ["Saab", "Volvo", "BMW"];
  constructor(private api: ApiService) {
    this.getCategories();
  }
  getCategories = () => {
    this.api.getAllCategories().subscribe(
      data => {                  
        this.categories = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  productClicked = (product) => {
    console.log(product.slug);
    console.log(product.subcategories);
    this.api.getOneCategory(product.slug).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}

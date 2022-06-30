import { TestBed } from '@angular/core/testing';

import { HistoricPriceServiceService } from './historic-price-service.service';

describe('HistoricPriceServiceService', () => {
  let service: HistoricPriceServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HistoricPriceServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

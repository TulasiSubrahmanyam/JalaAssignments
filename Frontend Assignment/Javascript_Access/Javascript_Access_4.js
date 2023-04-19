class Counter {
    constructor() {
      this._count = 0;
    }
    
    get count() {
      return this._count;
    }
    
    set count(value) {
      if (value < 0) {
        throw new Error('Counter value cannot be negative');
      }
      this._count = value;
    }
    
    increment() {
      this.count++;
    }
    
    decrement() {
      this.count--;
    }
  }
  
  const counter = new Counter();
  console.log(counter.count); // output: 0
  counter.increment();
  console.log(counter.count); // output: 1
  counter.decrement();
  console.log(counter.count); // output: 0
  
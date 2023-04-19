const car = {
    make: "Toyota",
    model: "Corolla",
    year: 2019,
    color: "silver"
  };
  
  for (let prop in car) {
    console.log(`${prop}: ${car[prop]}`);
  }
const numbers = [2, 5, 8, 11, 14];

let sum = 0;
  
for (let i in numbers) {
    sum += numbers[i];
  }
  
console.log("Total Sum",sum);
  
let num = 10;
let result;

switch (num % 2) {
  case 0:
    result = "Even";
    break;
  case 1:
    result = "Odd";
    break;
  default:
    result = "Invalid input";
}

console.log(result); // output: Even

function greeting(message) {
    console.log(message + " " + this.name);
  }
  
  const person1 = { name: "Alice" };
  const person2 = { name: "Bob" };
  
  // using call()
  greeting.call(person1, "Hello"); // output: Hello Alice
  greeting.call(person2, "Hi"); // output: Hi Bob
  
  // using apply()
  greeting.apply(person1, ["Hello"]); // output: Hello Alice
  greeting.apply(person2, ["Hi"]); // output: Hi Bob
  
function Person(name, age) {
    this.name = name;
    this.age = age;
  }
  
  // Add a new property to the Person constructor function
  Person.prototype.gender = 'Unknown';
  
  // Create a new instance of the Person object
  const person = new Person('John', 30);
  
  // Access the newly added property
  console.log(person.gender); // Output: Unknown
  
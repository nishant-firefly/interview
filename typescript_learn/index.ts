//Install node 21.7.3
// npm install -g typescript 
// tsc index.ts && node index.js # To run the script 
let age: number = 30; 
function greet(name: string): string{
    return `Hello ${name}`;
}
interface Person{
    name: string; 
    age: number; 
    greet(): string; // Note its an method but above are properties
}
// Classes, public , private, protected. 
class Student {
    constructor(public name: string, private grade: string ){
        this.name = name; 
        this.grade = grade; 

    }
    getInfo(): string{
        return `${this.name} is in ${this.grade} `;
    }
}
let student: Student = new Student(`Nishant`, `Fifth Grade`);
console.log(student.getInfo());


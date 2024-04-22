// Classes, public , private, protected. 
class Student {
    constructor(public name: string, private grade: string) {
        this.name = name;
    }
    getInfo(): string {
        return `${this.name} is in `;
    }
}
let student: Student = new Student(`Nishant`, `Fifth Grade`);


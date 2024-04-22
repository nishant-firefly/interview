//Install node 21.7.3
// npm install -g typescript 
var age = 30;
function greet(name) {
    return "Hello ".concat(name);
}
// Classes, public , private, protected. 
var Student = /** @class */ (function () {
    function Student(name, grade) {
        this.name = name;
        this.grade = grade;
        this.name = name;
        this.grade = grade;
    }
    Student.prototype.getInfo = function () {
        return "".concat(this.name, " is in ").concat(this.grade, " ");
    };
    return Student;
}());
var student = new Student("Nishant", "Fifth Grade");
console.log(student.getInfo());

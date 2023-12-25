// Задание 1 //
let apple = 10;

console.log(apple);
alert(apple);

let condition = "Text";

console.log("Good game is " + condition);

//Задание 2 //
let someInt = 341;

let someString = '100';

let someBool = true;

console.log(someInt + someString);
console.log(someInt + someBool);
console.log(someString + someInt);
console.log(someString + someBool);
console.log(someBool + someInt);
console.log(someBool + someString);

//Задание 3 //
let array = [];

for (let i = 0; i < 10; i++) {
    array.push(Math.floor(Math.random() * 21) - 10);
}

array = array.filter(num => num >= 0);

console.log(array);

//Задание 4 //
function getRandomNumber() {
    return Math.floor(Math.random() * 100000);
}

console.log(getRandomNumber());

function multiplyArray(arr, num) {
    return arr.map(element => element * num);
}

let myArray = [1, 2, 3, 4, 5];
let multipliedArray = multiplyArray(myArray, 3);
console.log(multipliedArray);

let generateRandomWord = function() {
    let words = ["яблоко", "банан", "что-то", "что-то2", "нет", "слово", "да"];
    return words[Math.floor(Math.random() * words.length)];
};

console.log(generateRandomWord());

//Задание 5 //
let person = {
    firstName: "Иван",
    surname: "Иванов",
    patronymic: "Иванович",
    birthday: "1985-10-25",
    hobby: "Чтение",
    group: "B",
    getInfo: function() {
        let today = new Date();
        let birthYear = new Date(this.birthday).getFullYear();
        let age = today.getFullYear() - birthYear;
        return `ФИО: ${this.surname} ${this.firstName} ${this.patronymic}, Год рождения: ${birthYear}, Хобби: ${this.hobby}, Возраст: ${age}`;},
};

alert(person.getInfo());

let salaries = {
    "Иванов": 50000,
    "Петров": 60000,
    "Сидоров": 55000,
    "Козлов": 65000,
    "Смирнов": 70000,
    "Федоров": 45000,
    "Михайлов": 48000,
    "Николаев": 52000,
    "Андреев": 53000,
    "Сергеев": 58000
};

let totalSalary = 0;
for (let key in salaries) {
    totalSalary += salaries[key];
}

console.log("Общая зарплата сотрудников:", totalSalary);


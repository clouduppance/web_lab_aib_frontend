// Задание 1 //

var firstVar = prompt('Введите первую перменную');
var secondVar = prompt('Введите вторую перменную');

if (firstVar === secondVar) {
    console.log('Переменные равны');
} else {
    console.log('Переменные не равны');
}

var worldString = 'world';
var combinedString = firstVar + worldString;

//Задание 2 //

var fruits = ['apple', 'strawberry', 'blueberry', 'raspberry', 'lemon'];

for (var i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);

    switch (fruits[i]) {
        case 'apple':
            console.log('apple green');
            break;
        case 'strawberry':
            console.log('strawberry red');
            break;
        case 'blueberry':
            console.log('blueberry blue');
            break;
        case 'raspberry':
            console.log('raspberry light red');
            break;
        case 'lemon':
            console.log('lemon yellow');
            break;
        default:
            break;
    }
}

//Задание 3 //

var numberOfPeople = parseFloat(prompt('Введите кол-во человек', undefined));

while (isNaN(numberOfPeople) || numberOfPeople === 0) {
  numberOfPeople = parseFloat(prompt('Введите корректное количество человек', undefined));
}

var salaryPerPerson = parseFloat(prompt('Введите зарплату на человека', undefined));

while (isNaN(salaryPerPerson) || salaryPerPerson === 0) {
  salaryPerPerson = parseFloat(prompt('Введите корректную зарплату на человека', undefined));
}

alert('Затраты на ЗП: ' + numberOfPeople * salaryPerPerson);

//Задание 4 //

var students = [
    { FIO: 'Петров А.А.', Ocenka: 5 },
    { FIO: 'Иванов Б.Б.', Ocenka: 3.4 },
    { FIO: 'Сидоров Г.Г.', Ocenka: 9 },
    { FIO: 'Немолодой Д.Д', Ocenka: 2 },
    { FIO: 'Молодой Е.Е', Ocenka: 3.4 }
];

var totalScore = 0;
var count = 0;
var poorStudents = [];

for (var i = 0; i < students.length; i++) {
    var currentScore = students[i].Ocenka;

    if (currentScore > 5 || currentScore < 0) {
        console.log('This value will not be considered as it does not meet the acceptable values');
        continue;
    }

    if (currentScore < 4) {
        poorStudents.push(students[i]);
    }

    totalScore += currentScore;
    count++;
}

var averageScore = totalScore / count;
console.log('Average score: ' + averageScore);

console.log('Poor students:');
if (poorStudents.length === 0) {
    console.log('None');
} else {
    poorStudents.forEach((student) => {
        console.log('FIO: ' + student.FIO + '; Score: ' + student.Ocenka);
    });
}



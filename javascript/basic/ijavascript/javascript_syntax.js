console.log('test1');
console.log('test2');
console.log('test3');
// JavaScript 


// 1. 변수 선언: RAM을 사용하는 문법
// 2. 데이터 타입: RAM을 '효율적'으로 사용하는 문법
// 3. 연산자: CPU 사용하는 문법
// 4. 조건문: 조건에 따라 코드를 효율적으로 실행하는 문법
// 5. 반복문: 반복되는 코드를 효율적으로 관리하는 문법
// 6. 함수: 중복 코드를 묶어서 효율적으로 관리하는 문법
// 7. 객체: (python에서는 class, data type) 식별자 1개에 데이터 여러개 저장 (데이터 타입 뿐만 아니라 함수도 포함)


// 1. 변수 선언
// 식별자: 저장공간을 구별하는 문자열 (즉, 변수명)
// 식별자 규칙: 대소문자, 숫자 _, $ 숫자 가장 앞에 안됨. 
// 식별자 컨벤션: (틀려도 에러는 안나지만 지켜야 할 규칙)
// -> 상수를 사용할 때는 (Upper_snake_case), 변수, 함수(camelCase), module(PascalCase)

// 식별자 1개, 데이터 1개
var data1 = 10;
var data2 = 'js';
// 인터프리터 언어 특징: 동적 타이핑, 데이터 타입의 선언 없이 자동으로 데이터 타입 선언


// 식별자 n개, 데이터 n개
var data3 = 20, 
    data4 = 'node';

// 식별자 n개, 데이터 1개
var data5 = data6 = 'web';
console.log(data1, data2, data3, data4, data5, data6);

// 2. data type (5가지 타입)
// 1) number: 숫자 타입
// 2) string: 문자열
// 3) boolean: 논리값: true, false (파이썬과 다르게 소문자로 시작)
// 4) function: 코드 저장하는 함수 데이터 타입
// 5) object: 객체를 저장하는 데이터 타입

var data1 = 1;
var data2 = 'str';
var data3 = false;
var data4 = function(){ console.log('function')};
var data5 = {key: 'value'}; // javascript는 키 값을 꼭 문자열로 사용하지 않아도 됨. 그 자체로 key 라고 인식함.

console.log(typeof data1, typeof data2, typeof data3, typeof data4, typeof data5)


// 2-2. 없는 데이터 표현
// undefined, null, NaN
// undefined: 선언 되었으나 값이 할당되지 않음
// null: 선언이 되어 값이 'null'로 할당됨
// NaN: number 데이터타입에서 데이터 없음.

var data1 = undefined;
var data2 = null;
var data3 = NaN;

console.log(typeof data1, typeof data2, typeof data3);

// 3. 연산자
// 산술: 데이터 + 데이터 => 데이터
// 비교: 데이터 + 데이터 => 논리값, 조건이 1개일 때 사용/ ==와 ===가 다름
// 논리: 논리값 + 논리값 => 논리값, 조건이 2개이상 사용
// 할당: 변수(식별자) 산술 => 변수에 누적해서 연산 (?)
// 삼항: condition ? ture : false : 간단한 조건문을 구현


// 4. 비교
// ===, ==
var data1 =1, data2 = '1';
console.log(typeof data1, data1, typeof data2, data2);
console.log(data1==data2, data1===data2); // ==는 데이터 내용만 비교, ===는 데이터 타입까지 비교
// 주로 === (3개)를 사용함.

// 논리 연산자: &&, ||, !

// 퀴즈 1: 예금잔고에서 인출금액을 인출가능하면 true, 불가능하면 false
var balance = 10000,
    withdraw = 6000;

console.log(balance >= withdraw);
//퀴즈 2: 1회 최대 인출금액이 5000원 조건
console.log((balance >= withdraw) && (withdraw <= 5000));

// 5. 조건문
// if, else if, else
// if(condition){코드}
// 퀴즈: 예금잔고에서 인출금액이 인출가능하면 '인출가능' 출력 코드 작성
var balance = 10000,
    withdraw = 6000;

if(balance >= withdraw){
    console.log('인출 가능');
}else{
    console.log('인출 불가능');
};

// 퀴즈 3.  최대 인출금액 5000원 조건을 추가
var balance = 10000,
    withdraw = 3000;

if(balance <= withdraw){
    console.log('인출 불가능');
}else if(withdraw >= 5000){
    console.log('최대 인출금액 초과');
}else{
    console.log('인출 가능')
};

// 6. 반복문
// while, for, break, continue

// while(condition) -> condition이 false가 될때까지 실행
var count = 3;
while(count>0){
    count -= 1;
    console.log(count , 'js')
}

// for
for(i=0; i<3; i++){
    console.log(i, 'js')
}

// 로또 번호 출력: 중복을 허용
// 조건 1: 1~45 사이에 랜덤한 숫자를 출력
// 조건 2: 6번 반복해야 함
// 조건 3: 중복을 허용

var count = 6, lotto = '';

for(var i=0; i < count; i++){
    var randNumber = Math.random();
    lotto += Math.ceil(randNumber*44) + 1 + ' ';
};
console.log(lotto);

// 6. 함수 : function
// 중복코드를 묶어서 코드 작성 및 실행
/// 사용법: 함수 선언 > 함수 호출(코드 실행)

function show_lotto(count){
    var lotto='';
    for (var i=0; i<count; i++){
        var randNumber = Math.ceil((Math.random() * 44)) + 1;
        lotto += randNumber + ' ';
    };
    console.log(lotto);
};

show_lotto(6);


// 함수선언 1: 함수 선언식
// 일반적인 사용법
// 코드의 최상단으로 올라가서 선언됨. -> 호이스팅
// 반드시 우선 선언됨.
function plus1(n1, n2){
    return n1 + n2;
}
// 함수선언 2: 함수 표현식
// 함수를 변수처럼 사용
// 코드의 순서대로 실행됨. 
var plus2 = function(n1, n2){
    return n1 + n2;
}
console.log(plus2(1, 2));


// 익명함수
// 선언과 동시에 호출하는 함수

// 일단 일반적인 방법
function minus1(n1, n2){
    return n1 - n2;
};

console.log(minus1(3,6));

// 익명함수
// 함수 생성을 괄호로 감쌈
(function minus2(n1, n2){
    console.log(n1 - n2);
}(4, 9));

// scope : 
// 함수 안과 함수 밖에서 선언된 변수는 다른 영역의 메모리를 사용함.
// 함수 안 : local, 지역
// 함수 밖 : global, 전역

var data = 10;

function change(){
    // var data = 20;
    // 만약 global로 사용하고 싶다면 외부 변수를 호출하면 됨.
    data = 20;

    // let으로 구별하기도 함. 
}
change();
console.log(data);

// 객체
// array: 배열 / python - list
// Class: 클래스 / python - class

var arr = [1, 2, 3, 'a', 'b'];
console.log(typeof arr, arr, arr[0]);

arr.push('c');
console.log(arr);

// 객체 생성 1
// dictionary 처럼 생성하는 방법
var account = {
    balance: 10000,
    withdraw: function(amount){
        account.balance -= amount;
    },
}

account.withdraw(1000);
console.log(account.balance);

// 객체 생성 2
// 함수를 사용해서 생성할 때, 이 경우 대문자로 시작
function Person(name){
    this.name = name
}

var person = new Person('Tom'); // 새로운 instance 생성에는 new를 사용함.
console.log(person.name);

// 클래스는 "하나의 목적 아래 모여있는 변수와 함수의 집합체"라고 생각하자.



// json 객체 : 웹 서비스에서 데이터를 주고 받을 때 사용하는 포멧
// 웹서비스에서는 문자열만 사용 가능하기 때문
// 객체 -> 문자열
var data ={
    name: 'Tom',
    addr: 'Seoul',
};
console.log(typeof data);
var json = JSON.stringify(data);
console.log(typeof json);


// 문자열 -> 객체
var jsonObj = JSON.parse(json);
console.log(typeof jsonObj, jsonObj);

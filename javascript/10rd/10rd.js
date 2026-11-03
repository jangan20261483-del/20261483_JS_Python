
var now = new Date();
var firstDay = new Date(2006, 7, 9);

// 시작 날짜 화면에 표시
document.querySelector("#startDate").innerText = "2006-08-09";

var toNow = now.getTime();
var toFirst = firstDay.getTime();

var passedTime = toNow - toFirst;
var passedDay = Math.floor(passedTime / (24 * 60 * 60 * 1000));

// 태어난 지 며칠인지 표시
document.querySelector("#accent").innerText = passedDay + "일";

// 기념일 계산
calcDate(100);
calcDate(200);
calcDate(365);
calcDate(500);
calcDate(700);
calcDate(1000);

function calcDate(days) {
    var someday = new Date(2006, 7, 9 + days);

    var year = someday.getFullYear();
    var month = someday.getMonth() + 1;
    var date = someday.getDate();

    document.querySelector("#date" + days).innerText =
        year + "년 " + month + "월 " + date + "일";
}

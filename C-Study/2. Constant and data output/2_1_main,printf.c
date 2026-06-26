/* 1. 프로그램과 main 함수 구조
함수 : 일정한 기능을 수행하는 코드 단위.
(main 함수는 프로그램의 시작을 의미하며 프로그램에 반드시 있어야함)
 */
// 작성자 : 이주현
//    제목 : 10과 20을 더하는 프로그램

// int main (void)
// {
//     10 + 20; // 10과 20을 더함

//     return 0; // 프로그램 종료
// }

/* main 함수 구조
7행 부터 12 행까지가 main 함수이며 머리와 몸통으로 구성.
머리 : 함수 원형이라고 하며, 함수 이름과 필요한 데이터 등을 표시
몸통 : {}(중괄호)안에 함수에서 실행할 일들을 작성, 몸통의 마지막에는 return 0;를 넣어 프로그램을 종료

 [몸통 프로그램 작성 규칙
1) 세미콜론을 사용해 문장의 끝을 표시
세미콜론은 문장의 마침표와 같은 역활

2) 한 줄에 한 문장씩 작성
한 줄에 세미콜론을 이용해 여러 코드를 작성할 수 있지만, 가독성을 위해 한 줄씩 작성

3) 일정한 간격으로 들여 쓰기
들여 쓰는 간격은 정해져 있진 않음, 보통 4자리 띄우기



2. 출력 함수 printf(문자열 출력하기)
화면에 데이터를 출력할 때는 printf 함수를 사용
print formatted라는 뜻 */

// #include <stdio.h> // stdio.h를 불러옴(stdio.h: standard input output을 의미)

// int mai(void)
// {
//     printf("Be happy"); //Bw happy 출력
//     printf("My friend"); // My friend 출력
//     return 0;
// }



/* 3. 제어 문자 출력
제어 문자 : 문자는 아니지만, 출력 방식에 영향을 주는 문자를 의미
백슬레시와 함께 사용 */
// #include <stdio.h>

// int main(void)
// {
//     printf("Be happy\n"); 
//     printf("1234567890\n");
//     printf("My\tfriend\n"); 
//     printf("Goot\bd\tchance\n"); 
//     printf("Cow\rW\a\n"); 

//     return 0;
// }

/* 

1) \n(개행, new line) : 줄 바꿈
2) \b(백스페이스, backspace) : 한 칸 왼쪽으로 이동
printf("Goot\bd\tchance\n")  goot에서 왼쪽으로 한칸 이동후에 d 입력 하고, tap간격을 띄운 후 chance 입력 후 줄 바꿈 
3) \r(캐리지 리턴, carriage return) : 맨 앞으로 이동
printf("Cow\rW\a\n") Cow가 출력되고 맨 앞으로 이동 후 W출력, 벨소리를 낸 후 줄 바꿈
4) \a(알럿 경보, alert) : 벨소리



4. 정수와 실수 출력 
printf는 기본적으로 문자열을 출력하는 함수. 따라서 숫자를 출략할 떈 변환문자를 사용해서 문자열로 변환하는 과정 필요.
정수는 d%, 실수는 %lf를 사용.(d는 decimal, lf는 long float를 의미함)
 */
// #include <stdio.h>
// int main(void)
// {
//     printf("%d\n", 10);   // %d의 위치에 10 출력
//     printf("%lf\n",3.4);   // %lf의 위치에 3.4를 소수점 이하 여섯째 자리까지 출력 
//     printf("%.1lf\n", 3.45);  // 소수점 이하 첫째 자리까지 출력(둘째 자리에서 반올림)
//     printf("%.10lf\n", 3.4);  // 소수점 이하 열째 자리 출력

//     printf("%d과 %d의 합은 %d입니다.\n", 10, 20, 10 + 20);
//     printf("%.1lf-%.1lf = %.1lf\n", 3.4, 1.2, 3.4 - 1.2);
// }



// 마무리
// - C 프로그램은 main 함수로 시작
// - //는 한 줄 주석문이고 /* */는 여러 줄을 한꺼번에 주석 처리하는 주석문
// - printf 함수는 데이터를 화면에 출력할 때 사용
// - 제어 문자를 문자열 안에 포함시키면 그 기능에 따라 출력 형태가 바뀜
// - printf 함수로 숫자를 출력할 때 정수는 %d, 실수는 %lf(기본은 6자리 까지 표현, %.xlf x자리까지 표현) 변환 문자를 사용


// 제어문자 정리 
// \n : 줄을 바꿈
// \t : 출력 위치를 다음 탭 위치로 옮김
// \r : 출력 위치를 줄의 맨 앞으로 옮김
// \b : 출력 위치를 한 칸 왼쪽으로 옮김
// \a : 벨소리를 냄

echo "# TIL" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zolriz/TIL.git
git push -u origin main
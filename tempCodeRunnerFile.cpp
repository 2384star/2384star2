const double RateKphMph =1.609344;
void main(){
    int kph;
    double mph;

    printf("당신의 구속을입력하시오");
    scanf("%d",&kph);
    mph = kph/RateKphMph;
    printf("당신의 구속은 %lf 입니다",mph);
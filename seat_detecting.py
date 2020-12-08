#from api import object_counting_api
import requests

#####1번: 전체 좌석 수와 들어온 사람 수 단순 계산#####
def seat_detecting_model1(cafe_seat,incount, outcount):
    total_passed_vehicle = incount - outcount
    if (total_passed_vehicle < 0):
        total_passed_vehicle = 0

    if(cafe_seat >= total_passed_vehicle):
        congestion = total_passed_vehicle/cafe_seat*100
    else:
        congestion = 100
    ###### 0(여유), 1(보통), 2(혼잡) 3단계######

    if(congestion < 20):
        real_time=0
    elif(congestion>=20 and congestion<60):
        real_time = 1
    elif(congestion>=60 and congestion <=100):
        real_time = 2

    return real_time

#####2번:
#def seat_detecting_model2(cafe_seat, total_passed_vehicle):





if __name__ == '__main__':
    real_time = seat_detecting_model(10,4)
    print(real_time)
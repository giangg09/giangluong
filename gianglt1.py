#---------------------------------------Hàm này dùng để đọc file (Task 1)----------------------------------------------------------------------------------------------------
from copyreg import pickle
import json
from pdb import line_prefix
import re
from os import lseek
from turtle import left

# Hàm so sánh mã SV không đúng tiêu chuẩn
def split_it(dulieu):
    regex= '([N]{1,1}[0-9]{8,8})'
    x =  re.findall(regex, dulieu)
    x = ''.join(x)
    if x == '':
        return True
    else:
        return False
# Hàm so sánh mã SV đúng tiêu chuẩn
def split_on(dulieu):
    regex= '([N]{1,1}[0-9]{8,8})'
    x =  re.findall(regex, dulieu)
    x = ''.join(x)
    if x == '':
        return False
    else:
        return True

def read_file(rf):
    with open (rf,'r') as file_object:
        data = file_object.read()
    return data

#Task  2
def phantich_dulieu(rf):
    with open(rf, 'r') as file_object:
        dem = 0
        check_dulieu = 0
        dong_dulieuloi = {}

        for line in file_object.readlines():
            dem = dem + 1
            ma_sv = line.split(',')[0]
            answer_sv = line.split(',')
            dem_socautraloi = len(answer_sv)

            if dem_socautraloi != 26 or split_it(ma_sv) == True:
                check_dulieu += 1
                dong_dulieuloi[dem] = line
    return dem, check_dulieu, dong_dulieuloi


def chamdiem(rf):
    answer_key = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
    danhsach_diem = dict()
    #Tao 2 list co san de luu bien dem moi cau bi sai hoac bo qua bao nhieu lan
    danhsach_sai = list(25)
    danhsach_boqua = list(25)
    with open(rf, 'r') as file_object:
        for line in file_object.readlines():
            ma_sv = line.split(',')[0]
            answer_sv = line.strip().split(',')[1:]
            diem = 0
            # Neu do dai chuoi cau tra loi = 25 thi se thuc hien so sanh
            if len(answer_sv) == 25 and split_on(ma_sv) == True:
                for i in range(25):
                    if answer_sv[i] == '':
                        danhsach_boqua[i] += 1
                    else:
                        if answer_key[i] == answer_sv[i]:
                            diem += 4
                        else:
                            diem -= 1
                            danhsach_sai[i] += 1
                danhsach_diemp[ma_sv] = diem
    # Ep kieu va khoi tao mot so list co san de luu cac ket qua can thiet
    lst_diem = list(map(float, danhsach_diem.values()))
    tonghop = list()
    cau_boqua = list()
    cau_sai = list()
    dem_soluongdiemcao = 0 
    tong_diem = 0

class BANGDIEM():
    #Constructer:
    def __init__(self, maHS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia):
        self.maHS = maHS
        self.Toan = Toan
        self.Ly = Ly
        self.Hoa = Hoa
        self.Sinh = Sinh
        self.Van = Van
        self.Anh = Anh
        self.Su = Su
        self.Dia = Dia
        #Load dữ liệu từ đường dẫn file vào một list.
    def load_dulieu(self, path):
        with open(path) as f:
            datalist = f.readlines()
            #print(datalist)
            return datalist
    def tinhdiem_trungbinh(self, path):
        data = self.load_dulieu(path)
        hs = [0]
        diemtb={'Toan':0,'Ly':0,'Hoa':0,'Sinh':0,'Van':0,'Anh':0,'Su':0,'Dia':0}
        bangdiem = dict()
        test=list()
        for i in data:
            if i.startswith('Ma HS'):
                continue
            hs=i.split(';')
            test.clear()
            #Tính Điểm trung bình của từng môn Tự nhiên và thêm phần tử vào list test
            for i in hs[1:5]:
                diem=i.split(',')
                diem_tbmon_tunhien=round(float(diem[0])*0.05+float(diem[1])*0.1+float(diem[2])*0.15+float(diem[3])*0.7,2)
                test.append(diem_tbmon_tunhien) 
            for i in hs[5:]:
                diem=i.split(',')
            #Tính điểm trung bình của từng môn Xã hội và thêm phần tử vào list test
                diem_tbmon_xahoi=round(float(diem[0])*0.05+float(diem[1])*0.1+float(diem[2])*0.1+float(diem[3])*0.15+float(diem[4])*0.6,2)
                test.append(diem_tbmon_xahoi)
            #Gán giá trị điểm trung bình từng môn vào dict diemtb
            diemtb.update(Toan=test[0],Ly=test[1],Hoa=test[2],Sinh=test[3],Van=test[4],Anh=test[5],Su=test[6],Dia=test[7])
            t = dict()
            t = diemtb.copy()
            #Dict bangdiem là một dict lớn có key là Mã Học Sinh, value là dict nhỏ(key: môn học, value: điểm trung bình môn)
            # k là mã học sinh, dạng số thứ tự
            bangdiem[hs[0]] = t
        return bangdiem
    def luudiem_trungbinh(self, dest1, path):
        data = self.load_dulieu(path)
        data_dtb=open(dest1,mode='w+')
        #Duyệt từng dòng trong file data
        for line in data:
            if not line.startswith("Ma HS"):
                continue
            hs=line.split(',')
        #Duyệt các phần tử trong dòng đầu tiên bao gồm tên cột: MaHS, Ten mon hoc
            for i in hs:
                #Ghi vào file mới dòng đầu tiên bao gồm tên cột Mahs, ten mon hoc
                data_dtb.write(i)
            #Lấy điểm trung bình đã tính ở ham tinhdiem_trungbinh
            chung = self.tinhdiem_trungbinh(path)
            for k,v in chung.items():
                listdiem=list(v.values())
                #Biến đổi từ dict sang dạng list để lưu dữ liệu vào file mới theo đúng dạng
                str1=str(listdiem).replace(',',';')
                str2=str1.replace('[','')
                str3=str2.replace(']','\n')
                str4=';'.join([str(k),str3])
            #Lưu vào file mới
                data_dtb.write(str4)
        data_dtb.close()
class DANHGIA(BANGDIEM):
    def __init__(self, maHS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia):
        super().__init__(maHS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia)
    def xeploai_hocsinh(self,dest1):
        data = self.load_dulieu(dest1)
        hs = [0]
        dict_xeploai = dict()
        #Duyet tung dong trong file data
        for line in data:
            if line.startswith('Ma HS'):
                continue
            hs = line.split(';')
            #print(hs)
            dtb_chuan = round(((float(hs[1]) + float(hs[2]) + float(hs[3]) + float(hs[4]))*2 + float(hs[5]) + float(hs[6]) + float(hs[7]) + float(hs[8]))/11,2)
            #print(dtb_chuan)
            xeploai = ''
            if dtb_chuan >= 9.0 and float(hs[1]) >= 8.0 and float(hs[2]) >= 8.0 and float(hs[3])>= 8.0 and float(hs[4]) >= 8.0 and float(hs[5]) >= 8.0 and float(hs[6]) >= 8.0 and float(hs[7]) >= 8.0 and float(hs[8]) >= 8.0 :
                xeploai = 'Xuat sac'
            elif dtb_chuan >=8.0 and float(hs[1]) >= 6.5 and float(hs[2]) >= 6.5 and float(hs[3]) >= 6.5 and float(hs[4]) >= 6.5 and float(hs[5]) >= 6.5 and float(hs[6]) >= 6.5 and float(hs[7]) >= 6.5 and float(hs[8]) >= 6.5 :
                xeploai = 'Gioi'
            elif dtb_chuan >= 6.5 and float(hs[1]) >= 5.0 and float(hs[2]) >= 5.0 and float(hs[3]) >= 5.0 and float(hs[4]) >= 5.0 and float(hs[5]) >= 5.0 and float(hs[6]) >= 5.0 and float(hs[7]) >= 5.0 and float(hs[8]) >= 5.0 :
                xeploai = 'Kha'
            elif dtb_chuan >= 6.0 and float(hs[1]) >= 4.5 and float(hs[2]) >= 4.5 and float(hs[3]) >= 4.5 and float(hs[4]) >= 4.5 and float(hs[5]) >= 4.5 and float(hs[6]) >= 4.5 and float(hs[7]) >= 4.5 and float(hs[8]) >= 4.5  :
                xeploai = 'TB Kha'
            else:
                xeploai = "TB"
            #print(xeploai)
            t = dict()
            t[hs[0]] = xeploai
            dict_xeploai.update(t)
        return dict_xeploai
    def xeploai_thidaihoc_hocsinh(self, dest1):
        data = self.load_dulieu(dest1)
        list_xeploai_thidaihoc = list()
        dict_xeploai_thidaihoc = dict()
        #Tính toán các điểm theo khối thi Đại hoc và được 1 dictionary dict_thidaihoc_hocsinh
        for line in data:
            if line.startswith('Ma HS'):
                    continue
            hs = line.split(';')
            list_xeploai_thidaihoc.clear()
            #Tính điểm khối A
            diemA = round( (float(hs[1]) + float(hs[2]) + float(hs[3]))  ,2)
            #print(diemA)
            if diemA >= 24:
                list_xeploai_thidaihoc.append(1)
            elif diemA < 24 and diemA >=18:
                list_xeploai_thidaihoc.append(2)
            elif diemA < 18 and diemA >= 12:
                list_xeploai_thidaihoc.append(3)
            elif diemA < 12:
                list_xeploai_thidaihoc.append(4) 
            #Tính điểm khối A1
            diemA1 = round( (float(hs[1]) + float(hs[2]) + float(hs[6]))  ,2)
            #print(diemA1)
            if diemA1 >= 24:
                list_xeploai_thidaihoc.append(1)
            elif diemA1 < 24 and diemA1 >=18:
                list_xeploai_thidaihoc.append(2)
            elif diemA1 < 18 and diemA1 >= 12:
                list_xeploai_thidaihoc.append(3)
            elif diemA1 < 12:
                list_xeploai_thidaihoc.append(4) 
            #Tính điểm khối B
            diemB = round( (float(hs[1]) + float(hs[3]) + float(hs[4]))  ,2)
            #print(diemB)
            if diemB >= 24:
                list_xeploai_thidaihoc.append(1)
            elif diemB < 24 and diemB >=18:
                list_xeploai_thidaihoc.append(2)
            elif diemB < 18 and diemB >= 12:
                list_xeploai_thidaihoc.append(3)
            elif diemB < 12:
                list_xeploai_thidaihoc.append(4) 
            #Tính điểm khối C
            diemC = round( (float(hs[5]) + float(hs[7]) + float(hs[8])) ,2)
            #print(diemC)
            if diemC >= 21:
                list_xeploai_thidaihoc.append(1)
            elif diemC < 21 and diemC >=15:
                list_xeploai_thidaihoc.append(2)
            elif diemC < 15 and diemC >= 12:
                list_xeploai_thidaihoc.append(3)
            elif diemC < 12:
                list_xeploai_thidaihoc.append(4) 
            #Tính điểm khối D
            diemD = round( (float(hs[1]) + float(hs[5]) + float(hs[6])*2)  ,2)
            #print(diemD)
            if diemD >= 32:
                list_xeploai_thidaihoc.append(1)
            elif diemD < 32 and diemD >=24:
                list_xeploai_thidaihoc.append(2)
            elif diemD < 24 and diemD >= 20:
                list_xeploai_thidaihoc.append(3)
            elif diemD < 20:
                list_xeploai_thidaihoc.append(4) 
            #print(list_xeploai_thidaihoc)
            t = list()
            t= list_xeploai_thidaihoc.copy()
            u = dict()
            u[hs[0]]=t
            dict_xeploai_thidaihoc.update(u)
            #list_xeploai_thidaihoc.clear()
        return dict_xeploai_thidaihoc
class TUNHIEN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self, dest1):
        data = self.load_dulieu(dest1)
        list_xeploai_thidaihoc = list()
        dict_xeploai_thidaihoc = dict()
        #Tính toán các điểm theo khối thi Đại hoc và được 1 dictionary dict_thidaihoc_hocsinh
        for line in data:
            if line.startswith('Ma HS'):
                    continue
            hs = line.split(';')
            list_xeploai_thidaihoc.clear()
                #Tính điểm khối A
            diemA = round( (float(hs[1]) + float(hs[2]) + float(hs[3]))  ,2)
            #print(diemA)
            if diemA >= 24:
                list_xeploai_thidaihoc.append(1)
            elif diemA < 24 and diemA >=18:
                list_xeploai_thidaihoc.append(2)
            elif diemA < 18 and diemA >= 12:
                list_xeploai_thidaihoc.append(3)
            elif diemA < 12:
                list_xeploai_thidaihoc.append(4) 
                #Tính điểm khối A1
            diemA1 = round( (float(hs[1]) + float(hs[2]) + float(hs[6]))  ,2)
            #print(diemA1)
            if diemA1 >= 24:
                    list_xeploai_thidaihoc.append(1)
            elif diemA1 < 24 and diemA1 >=18:
                list_xeploai_thidaihoc.append(2)
            elif diemA1 < 18 and diemA1 >= 12:
                    list_xeploai_thidaihoc.append(3)
            elif diemA1 < 12:
                    list_xeploai_thidaihoc.append(4) 
                #Tính điểm khối B
            diemB = round( (float(hs[1]) + float(hs[3]) + float(hs[4]))  ,2)
            #print(diemB)
            if diemB >= 24:
                list_xeploai_thidaihoc.append(1)
            elif diemB < 24 and diemB >=18:
                    list_xeploai_thidaihoc.append(2)
            elif diemB < 18 and diemB >= 12:
                    list_xeploai_thidaihoc.append(3)
            elif diemB < 12:
                    list_xeploai_thidaihoc.append(4) 
            t = list()
            t= list_xeploai_thidaihoc.copy()
            #print(t)
            u = dict()
            u[hs[0]]=t
            dict_xeploai_thidaihoc.update(u)
            #list_xeploai_thidaihoc.clear()
        #print(dict_xeploai_thidaihoc)
        return dict_xeploai_thidaihoc 
class XAHOI(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self, dest1):
        data = self.load_dulieu(dest1)
        list_xeploai_thidaihoc = list()
        dict_xeploai_thidaihoc = dict()
        #Tính toán các điểm theo khối thi Đại hoc và được 1 dictionary dict_thidaihoc_hocsinh
        for line in data:
            if line.startswith('Ma HS'):
                    continue
            hs = line.split(';')
            list_xeploai_thidaihoc.clear()
                #Tính điểm khối C
            diemC = round( (float(hs[5]) + float(hs[7]) + float(hs[8])) ,2)
            #print(diemC)
            if diemC >= 21:
                    list_xeploai_thidaihoc.append(1)
            elif diemC < 21 and diemC >=15:
                list_xeploai_thidaihoc.append(2)
            elif diemC < 15 and diemC >= 12:
                    list_xeploai_thidaihoc.append(3)
            elif diemC < 12:
                    list_xeploai_thidaihoc.append(4)
            t = list()
            t= list_xeploai_thidaihoc.copy()
            u = dict()
            u[hs[0]]=t
            dict_xeploai_thidaihoc.update(u)
        return dict_xeploai_thidaihoc  
class COBAN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self, dest1):
        data = self.load_dulieu(dest1)
        list_xeploai_thidaihoc = list()
        dict_xeploai_thidaihoc = dict()
        #Tính toán các điểm theo khối thi Đại hoc và được 1 dictionary dict_thidaihoc_hocsinh
        for line in data:
            if line.startswith('Ma HS'):
                    continue
            hs = line.split(';')
            list_xeploai_thidaihoc.clear()
                #Tính điểm khối D
            diemD = round( (float(hs[1]) + float(hs[5]) + float(hs[6])*2)  ,2)
            #print(diemD)
            if diemD >= 32:
                list_xeploai_thidaihoc.append(1)
            elif diemD < 32 and diemD >=24:
                list_xeploai_thidaihoc.append(2)
            elif diemD < 24 and diemD >= 20:
                list_xeploai_thidaihoc.append(3)
            elif diemD < 20:
                list_xeploai_thidaihoc.append(4)
            t = list()
            t= list_xeploai_thidaihoc.copy()
            u = dict()
            u[hs[0]]=t
            dict_xeploai_thidaihoc.update(u)
            #list_xeploai_thidaihoc.clear()
        return dict_xeploai_thidaihoc
def main():
    path = 'diem_chitiet.txt'
    vidu = DANHGIA(0,0,0,0,0,0,0,0,0)
    #BANGDIEM.load_dulieu(vidu,path)
    #print(BANGDIEM.tinhdiem_trungbinh(vidu,path))
    dest1 = 'diem_trungbinh.txt'
    BANGDIEM.luudiem_trungbinh(vidu,dest1,path)
    #print(DANHGIA.xeploai_hocsinh(vidu,dest1))
    dest2 = 'danhgia_hocsinh.txt'
    # print(DANHGIA.xeploai_thidaihoc_hocsinh(vidu,dest1))
    tunhien = TUNHIEN(0,0,0,0,0,0,0,0,0)
    print(TUNHIEN.xeploai_thidaihoc_hocsinh(tunhien,dest1))
    xahoi = XAHOI(0,0,0,0,0,0,0,0,0)
    print(XAHOI.xeploai_thidaihoc_hocsinh(xahoi,dest1))
    coban = COBAN(0,0,0,0,0,0,0,0,0)
    print(COBAN.xeploai_thidaihoc_hocsinh(coban,dest1))
    data_xeploai=open('danhgia_hocsinh.txt',mode='w+')
    xeploai = DANHGIA.xeploai_hocsinh(vidu,dest1)
    thidaihoc = DANHGIA.xeploai_thidaihoc_hocsinh(vidu,dest1)
    #Hàng đầu tiên của file “danhgia_hocsinh.txt” gồm các trường: “Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”.
    data_xeploai.write('Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n')
    #Hàng thứ 2 theo VD sau: “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.
    for i in range(len(xeploai) + 1):
        if i == 0:
            continue
        a = xeploai.get(str(i))
        #Chuyển đổi dữ liệu trong xếp loại thi ĐH từ số sang string để join thidaihoc.get(i) từ list sang string
        k = list()
        for j in thidaihoc.get(str(i)):
            k.append(str(j))
        c = ','.join(k)
        data_xeploai.write('{} {} {}\n'.format(i, a, c))
    data_xeploai.close()
main()


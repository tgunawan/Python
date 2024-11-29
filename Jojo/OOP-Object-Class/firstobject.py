#--------------library----------------
import os,time

'''class pemain:
    def __init__(self):
        self.name='Jojo'
        self.health=100

player=pemain()
player.health-=10
print(player.health)'''
#--------------class / function----------------
class mobil: # class untuk object mobil
    def __init__(self,model,merek,tahun):
        self.model=model
        self.merek=merek
        self.tahun=tahun
    
    def info(self): # fungsi / method untuk menampilkan informasi
        print(f'Mobil ini adalah model {self.model},dengan merek {self.merek} dan tahun {self.tahun}')

    def jalan(self):
        return f'{self.model} sedang berjalan broom broom'
    
    def start(self):
        print("Mobil di hidupkan")

    def stop(self):
        print("Mobil di matikan")

class mobilListrik(mobil):
    def __init__(self,model,merek,tahun,Baterai):
        super().__init__(model,merek,tahun)
        self.Baterai=Baterai

    def charge(self):
        print("Mobil ini sedang di isi baterai")

    # def stop(self):
    #     print("Mobil Listrik di matikan")

#--------------object / Variable----------------
mobil1=mobil("Bria","Hondi",2000)
mobil2=mobilListrik("Bigui","Wilung",2020,"1000watt")

#--------------main----------------
os.system('cls')
print(mobil1.tahun)
mobil1.info()
print(mobil1.jalan())

'''del mobil1 #delete object
del mobil1.tahun # delete attribute

print(mobil1.tahun)'''

mobil2.start()
mobil2.stop()
#--------------end----------------
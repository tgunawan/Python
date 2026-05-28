'''# decorator
def tampilduluan(func):
    def ngomong(*args, **kwargs):
        print("Hallo mulai")
        return func(*args, **kwargs)
    return ngomong
        
@tampilduluan
def penutupan():
    print("Terimakasih sudah hadir")
    
class speechpembuka:
    def __init__(self,nama):
        self.nama=nama
        pass

    @tampilduluan
    def pembukaan(self):
        print("Selamat datang di pertemuan ini")


pembicara=speechpembuka("test")

pembicara.pembukaan()
penutupan()'''

# decorator jika funcsi tanpa parameter
def tampilduluan(func):
    def ngomong():
        print("Hallo mulai")
        return func()
    return ngomong
        
@tampilduluan
def penutupan():
    print("Terimakasih sudah hadir")

penutupan()
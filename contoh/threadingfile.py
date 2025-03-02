'''import threading
import time

def fungsi_pertama():
    for i in range(5):
        print("Fungsi pertama:", i)
        time.sleep(1)

def fungsi_kedua():
    for i in range(5):
        print("Fungsi kedua:", i)
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=fungsi_pertama)
    thread2 = threading.Thread(target=fungsi_kedua)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Kedua fungsi telah selesai.")
'''
import asyncio
import time

async def fungsi_pertama():
    for i in range(5):
        print("Fungsi pertama:", i)
        await asyncio.sleep(1)  # Menangguhkan eksekusi coroutine

async def fungsi_kedua():
    for i in range(5):
        print("Fungsi kedua:", i)
        await asyncio.sleep(3)  # Menangguhkan eksekusi coroutine

async def main():
    await asyncio.gather(fungsi_pertama(), fungsi_kedua())

if __name__ == "__main__":
    asyncio.run(main())

    print("Kedua fungsi telah selesai.")
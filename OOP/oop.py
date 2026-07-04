""" pembataran

from abc import ABC, abstractmethod

# ==============================
# Abstraction
# ==============================
# Kita buat kelas abstrak 'Payment' yang mendefinisikan kerangka umum
# Semua metode pembayaran harus punya 'pay' tapi detailnya berbeda.
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # hanya kerangka, implementasi ada di subclass


# ==============================
# Polymorphism
# ==============================
# Subclass yang mengimplementasikan metode 'pay' dengan cara berbeda

class CreditCardPayment(Payment):
    def pay(self, amount):
        # Implementasi khusus untuk pembayaran dengan kartu kredit
        print(f"Pembayaran sebesar Rp{amount} menggunakan Kartu Kredit berhasil.")


class PayPalPayment(Payment):
    def pay(self, amount):
        # Implementasi khusus untuk pembayaran dengan PayPal
        print(f"Pembayaran sebesar Rp{amount} melalui PayPal berhasil.")


class BankTransferPayment(Payment):
    def pay(self, amount):
        # Implementasi khusus untuk pembayaran dengan transfer bank
        print(f"Pembayaran sebesar Rp{amount} lewat Transfer Bank berhasil.")


# ==============================
# Main Program
# ==============================
# Fungsi ini menerima objek Payment apapun
# Inilah contoh polymorphism: objek berbeda tapi diperlakukan sama
def process_payment(payment_method: Payment, amount: int):
    # Tidak peduli jenis payment, cukup panggil 'pay'
    payment_method.pay(amount)


# ==============================
# Testing
# ==============================
if __name__ == "__main__":
    # Membuat objek dari berbagai metode pembayaran
    cc = CreditCardPayment()
    paypal = PayPalPayment()
    bank = BankTransferPayment()

    # Semua objek bisa diproses dengan cara yang sama
    process_payment(cc, 100000)       # Output: Kartu Kredit
    process_payment(paypal, 250000)  # Output: PayPal
    process_payment(bank, 500000)    # Output: Transfer Bank
"""

from abc import ABC, abstractmethod

# ==============================
# Abstraction
# ==============================
# Kelas abstrak 'Character' mendefinisikan kerangka umum untuk semua karakter game.
# Semua karakter harus bisa 'attack', tapi cara menyerang berbeda-beda.
class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @abstractmethod
    def attack(self, target):
        pass  # hanya kerangka, implementasi ada di subclass


# ==============================
# Polymorphism
# ==============================
# Subclass yang mengimplementasikan metode 'attack' dengan cara berbeda

class Warrior(Character):
    def attack(self, target):
        damage = 15
        target.hp -= damage
        print(f"{self.name} menyerang {target.name} dengan pedang! Damage: {damage}. HP {target.name} sekarang {target.hp}")


class Mage(Character):
    def attack(self, target):
        damage = 20
        target.hp -= damage
        print(f"{self.name} melempar bola api ke {target.name}! Damage: {damage}. HP {target.name} sekarang {target.hp}")


class Archer(Character):
    def attack(self, target):
        damage = 10
        target.hp -= damage
        print(f"{self.name} menembakkan panah ke {target.name}! Damage: {damage}. HP {target.name} sekarang {target.hp}")


# ==============================
# Main Program
# ==============================
def battle_round(attacker: Character, defender: Character):
    # Fungsi ini menerima objek Character apapun
    # Inilah contoh polymorphism: objek berbeda tapi diperlakukan sama
    attacker.attack(defender)


# ==============================
# Testing
# ==============================
if __name__ == "__main__":
    # Membuat karakter
    hero = Warrior("Arthur", 100)
    enemy1 = Mage("Dark Sorcerer", 80)
    enemy2 = Archer("Goblin Archer", 60)

    # Simulasi battle
    battle_round(hero, enemy1)   # Warrior menyerang Mage
    battle_round(enemy1, hero)   # Mage menyerang Warrior
    battle_round(enemy2, hero)   # Archer menyerang Warrior

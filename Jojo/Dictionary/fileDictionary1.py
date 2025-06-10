#buat variable dictionary buku(title,author,year,genre)

# myBook={
#     'title':'Harry Potter',
#     'author':'J.K. Rowling',
#     'year':1997,
#     'genre':'fantasy'
# }
# myBook2={"title":"The Hobbit",
#         "author":"J.R.R. Tolkien",
#         "year":1937,
#         "genre":"fantasy"
# }
# myBook3={"title":"The Da Vinci Code",
#         "author":"Dan Brown",
#         "year":2003,
#         "genre":"mystery"
# }

'''# contoh  list of dictionary
myBooks=[myBook,myBook2,myBook3]
myBooks.append({"title":"The Alchemist",
                "author":"Paulo Coelho",
                "year":1988,
                "genre":"adventure"})
print("List of books:",myBooks)
myBooks[3]['title']="The Alchemist: A Graphic Novel"
print(myBooks[3]['title'])'''

# contoh dictionary of dictionary dictionary 2D
myBooks={"buku1":
            { 'title':'Harry Potter',
                'author':'J.K. Rowling',
                'year':1997,
                'genre':'fantasy'},
        "buku2":
            { 'title':'The Hobbit',
                'author':'J.R.R. Tolkien',
                'year':1937,
                'genre':'fantasy'},
        "buku3":
            { 'title':'The Da Vinci Code',
                'author':'Dan Brown',
                'year':2003,
                'genre':'mystery'}
}
'''
print("List of books:",myBooks['buku1']['year'])
print(len(myBooks))
for key in myBooks:
    print("key:",key)

for key in range(len(myBooks)):
    print("key:",key)'''

# print("Publisher:",myBook.get("publisher","Belum di input")) #jika key ada maka di tampilkan, jika tidak ada maka  menampilkan data default
# print("Full display Dictionary Item:",myBook,"\n")
# print("Title book 1:",myBook['publisher'])

'''#ini untuk buat key yang kosong
try:
    print("Title:",myBook['publisher'])
except KeyError:
    myBook["publisher"]="Gramedio"
    print("Key not found, and has been created")'''

# del myBook['title']#hapus dengan del
'''removetitle=myBook.pop('title',"Title not found")#hapus dengan pop
print("Removed Title:",removetitle)

tidakketemu=myBook.pop('title',"ga ada")
print("Title not found:",tidakketemu)
print(myBook)'''
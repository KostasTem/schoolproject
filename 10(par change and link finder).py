import urllib.request
website = input("Εισάγεται την ιστοσελίδα σε μορφή http://www.example.com:")
response = urllib.request.urlopen(website)
html = response.read()
counter1 = 0
counter2 = 0
l = list(html.split(b">"))
for i in range(len(l)):
    if b"<p" in l[i]:
        counter1 = counter1 + 1
    if b"<br" in l[i]:
        counter1 = counter1 + 1
    if b"http" in l[i]:
        counter2 = counter2 + 1
print("Υπάρχουν "+str(counter1)+" αλλαγές γραμμής")
print("\n")
print("Υπάρχουν "+str(counter2)+" σύνδεσμοι")

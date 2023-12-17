import turtle

def tobbszinu_negyzet_rajzolas(t, h):
  for i in ["red", "yellow", "green", "blue"]:
    t.color(i)
    t.forward(h)
    t.left(90)

# ablak létrehozása
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

# Tundi létrehozása
Tundi = turtle.Turtle()
Tundi.pensize(3)

meret = 20 # a legkisebb negyzet mérete

for i in range(15):
  tobbszinu_negyzet_rajzolas(Tundi, meret )
  meret = meret + 10 # növeljük a méretet
  Tundi.forward(10) # kicsit arréb léptetjük a Tundit
  Tundi.right(18)   # kicsit elfordítjuk a Tundit

ablak.mainloop()
  
  
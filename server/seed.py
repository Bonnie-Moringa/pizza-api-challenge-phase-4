from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# Seed Restaurants
r1 = Restaurant(name="Pizza Inn", address="Ruiru")
r2 = Restaurant(name="Dominos Pizza", address="Westlands")
r3 = Restaurant(name="Mambo Italia", address="ValleyRoad")
db.session.add_all([r1, r2, r3])

# Seed Pizzas
p1 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese")
p2 = Pizza(name="Chicken BBQ", ingredients="Dough, Tomato, Chicken")
db.session.add_all([p1, p2])
db.session.commit()

# Seed RestaurantPizzas
rp1 = RestaurantPizza(price=25, restaurant_id=r1.id, pizza_id=p1.id)
rp2 = RestaurantPizza(price=20, restaurant_id=r2.id, pizza_id=p2.id)
db.session.add_all([rp1, rp2])
db.session.commit()

print("Seeded database!")

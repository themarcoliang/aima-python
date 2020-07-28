This is a knowledge base that will list out suitable cars according to user's needs.

A few things that it needs before it's able to give a list of cars:

Seats: two_seats, five_seats, seven_seats
Doors: two_doors, four_doors
Trunk Space: large_trunk, small_trunk

To choose an option, simply "tell" the KB the choice (multiple choices possible)

Based on these three, the KB will choose from the follow category of cars:
sedan, coupe, suv, minivan, truck

Last two pieces of information required is:

Manufacturer Origin: american, japanese, european
Price Range (before taxes and options): budget (<$50,000), midrange ($50,000-$100,000), expensive ($100,000-$150,000),
very_expensive ($150,000-$300,000), ultra_expensive($300,000+)

Once all five options are filled out, running "infer_all" should give list of cars that fit the criteria

Please note that this 110-line database is by no way complete, many cars and categories have been omitted
to prevent this from getting way too complicated.

Also, since the KB program does not accept numbers, capitalized romanization is used in place
For example: McLaren 720s -> mclaren_SEVENTWOZEROs
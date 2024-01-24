from typing import Union
from recipe_scrapers import scrape_me

from fastapi import FastAPI

app = FastAPI()

recipes_urls = [
    "https://www.chefkoch.de/rezepte/3466261516440078/Kuemmelrotkraut-mit-Ofen-Suesskartoffeln.html",
    "https://www.chefkoch.de/rezepte/1631611270752104/Vegetarische-Frikadellen.html",
    "https://www.chefkoch.de/rezepte/2352371374010722/Cremiger-Nudelauflauf-mit-Tomaten-und-Mozzarella.html",
    "https://www.chefkoch.de/rezepte/802701184066929/Bester-vegetarischer-Nudelauflauf.html",
    "https://www.chefkoch.de/rezepte/745721177147257/Lasagne.html",
    "https://www.chefkoch.de/rezepte/2293251365606285/Bulgogi-mariniertes-koreanisches-Rindfleisch.html",
]

recipes_json = [
    {
        "difficulty": "medium",
        "imageUrl": "https://www.allrecipes.com/thmb/FRU2TAYiIx46zBS78OkZQlA-7Sc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8415794-crispy-smashed-potatoes-ddmfs-3x4-1170-7ac94913792a490dba38bac85c9a49bf.jpg",
        "info": "Crispy smashed potatoes are delicious, golden brown, crispy on the outside, fluffy on the inside, and these have an extra crispy layer of broiled Parmesan cheese on top.",
        "ingredients": [
            "1 1/2 pounds red skinned potatoes",
            "2 tablespoons olive oil, divided",
            "1/2 teaspoon salt, divided",
            "1/2 teaspoon ground black pepper, divided",
            "3 ounces Parmesan cheese, finely shredded (3/4 cup)",
            "2 tablespoons minced fresh Italian parsley",
        ],
        "instructions": [
            {
                "name": "Place potatoes in a large saucepan, and add enough water to cover by at least 1 inch. Bring to a boil. Reduce heat, cover, and simmer until potatoes are very tender, drain.",
                "time": 1200,
            },
            {
                "name": "Heat the oven to 230 degrees. Line a 15x10x1-inch baking pan with foil. Brush foil with 1 tablespoon olive oil.",
                "time": 0,
            },
            {
                "name": "Transfer potatoes to the prepared baking pan. Use a  glass to lightly press down on each potato to smash to about 1/2-inch thickness",
                "time": 0,
            },
            {
                "name": "Brush smashed potatoes with remaining 1 tablespoon olive oil. Sprinkle with 1/4 teaspoon salt and 1/4 teaspoon pepper.",
                "time": 0,
            },
            {
                "name": "Roast in the preheated oven, uncovered, until bottoms are lightly browned and crisp",
                "time": 900,
            },
            {
                "name": "Turn potatoes; sprinkle with the remaining 1/4 teaspoon salt and 1/4 teaspoon pepper. Return to the oven and roast until potatoes are lightly browned and crisp",
                "time": 900,
            },
            {
                "name": "Preheat the broiler and set a rack 4 to 5 inches from the heat source. Sprinkle Parmesan cheese over potatoes.",
                "time": 0,
            },
            {
                "name": "Broil until cheese is golden brown and crispy. Garnish with parsley.",
                "time": 180,
            },
        ],
        "name": "Crispy Smashed Potatoes",
        "servings": 6,
        "tags": ["Side Dish,Dinner"],
        "time": 60,
    },
    {
        "difficulty": "easy",
        "imageUrl": "https://www.allrecipes.com/thmb/lhJyok211mG7bkKgzAud3JMAg-8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/7629322_Baked-Feta-Cheese-and-Tomatoes_lutzflcat_4x3-c5c8db0f6d944c8494e6b3457cce71cc.jpg",
        "info": "This easy baked feta and tomatoes dish makes a great summer appetizer, combining sweet and salty flavors. Serve with crusty bread, pita chips, or crackers.",
        "ingredients": [
            "1 (7-oz) block of Greek feta cheese",
            "1 tablespoon honey",
            "drizzle of olive oil",
            "1-1/2 cups halved cherry or grape tomatoes",
            "1/3 cup halved Kalamata olives",
            "1/3 cup thinly sliced red onion",
            "2 tablespoons olive oil",
            "1 clove garlic, minced",
            "1 teaspoon dried oregano",
            "salt and freshly ground black pepper to taste",
            "chopped fresh basil for garnish (optional)",
        ],
        "instructions": [
            {"name": "Preheat the oven to 200 degrees C.", "time": 0},
            {
                "name": "Place the feta cheese in the center of a baking dish. Spread with honey and drizzle with olive oil.",
                "time": 0,
            },
            {
                "name": "In a small bowl, combine tomatoes, olives, red onion, olive oil, and garlic. Sprinkle with oregano, season with salt and pepper, and toss. Arrange the tomato mixture around the feta cheese.",
                "time": 0,
            },
            {
                "name": "Bake in the preheated oven until cheese is soft and tomato mixture is bubbly. If you want more color, briefly place under the broiler.",
                "time": 1800,
            },
            {
                "name": "Garnish with fresh basil, if desired, and serve warm.",
                "time": 0,
            },
        ],
        "name": "Baked Feta Cheese and Tomatoes",
        "servings": 6,
        "tags": ["Appetizer,Dinner"],
        "time": 20,
    },
    {
        "difficulty": "easy",
        "imageUrl": "https://www.allrecipes.com/thmb/27cEM2MRSneSgOe9FMkZd4De9Ic=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/7852451_Steak-and-Potatoes-Foil-Packs_CookingWithShelia_4x3-e7745462fd474af4af09b0c750601f38.jpg",
        "info": "These steak and potato foil packets are a fun dish that the whole family will love and an easy clean up. The combination of steak, potatoes, grilled onions, and bell peppers are seasoned to perfection.",
        "ingredients": [
            "1 pound Small Yukon Potatoes, halved",
            "1 1/2 pounds Sirloin Steak, cut into bite-sized strips",
            "1 Yellow Onion, sliced",
            "1 Red Bell Pepper, sliced",
            "1 Green Bell Pepper, sliced",
            "1 Carrot, thinly sliced",
            "4 tablespoons butter, or as needed",
            "steak seasoning, to taste",
            "5 to 6 cloves garlic, chopped",
        ],
        "instructions": [
            {
                "name": "Prepare an outdoor grill, preferably a charcoal grill, for medium-high heat.",
                "time": 0,
            },
            {
                "name": "Place potatoes in a microwave-safe dish and cook on high until they are tender with a bite",
                "time": 180,
            },
            {
                "name": "Divide steak, potatoes, onions, red and green bell pepper, and carrots evenly onto 4 to 6 squares of aluminum foil.",
                "time": 0,
            },
            {
                "name": " Add 1 tablespoon butter and a little fresh garlic to each pack; fold foil over the top to close each packet tightly.",
                "time": 0,
            },
            {
                "name": "Place foil packs on the hot side of the grill. Carefully open one foil pack to check for steak doneness.",
                "time": 300,
            },
            {
                "name": "Garnish with fresh basil, if desired, and serve warm.",
                "time": 0,
            },
        ],
        "name": "Steak and Potato Foil Packets",
        "servings": 4,
        "tags": ["Dinner,Entree"],
        "time": 30,
    },
    {
        "difficulty": "medium",
        "imageUrl": "https://www.allrecipes.com/thmb/GvUNRGCUX0VHJwTXs9I3AUjzVMc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/8347289-stuffing-bread-pudding-ddmfs-3x4-10775-5d743086a1d042e59babccf92241b863.jpg",
        "info": "Stuffing bread pudding is the perfect side to your Thanksgiving dinner. Use slightly stale bread, lightly toasted, for best results.",
        "ingredients": [
            "6 cups (8 ounces) 3/4-inch cubes soft sandwich bread",
            "1/4 cup unsalted butter",
            "1 1/2 cups chopped yellow onion (1 1/2 medium onions)",
            "1 cup chopped celery (2 medium stalks)",
            "3 cloves garlic, minced",
            "1 teaspoon dried thyme or 1 tablespoon chopped fresh thyme",
            "1 teaspoon dried sage or 1 tablespoon chopped fresh sage",
            "1 teaspoon dried rosemary or 1 tablespoon chopped fresh rosemary",
            "1 teaspoon salt",
            "1 teaspoon freshly ground black pepper",
            "2 tablespoon white wine vinegar",
            "1/4 cup chopped fresh parsley",
            "4 eggs, lightly beaten",
            "2 cups half-and-half",
            "4 ounces gouda cheese, shredded (1 cup)",
            "2 ounces grated Parmesan cheese (2/3 cup)",
        ],
        "instructions": [
            {
                "name": "Gather all ingredients. Preheat oven to 350 175 degrees C. Grease a 2-quart baking dish; set aside.",
                "time": 0,
            },
            {
                "name": "Spread bread on a large baking sheet. Bake until lightly golden and toasted, stirring once halfway through. Turn oven off.",
                "time": 1200,
            },
            {
                "name": "Melt butter in a large skillet over medium heat. Add onions and celery, cook stirring frequently, until translucent.",
                "time": 300,
            },
            {
                "name": "Add garlic, thyme, sage, rosemary, salt and pepper. Continue to cook and stir until garlic is aromatic. Add white wine vinegar and cook, stirring, until mostly evaporated",
                "time": 180,
            },
            {
                "name": "Combine toasted bread cubes, onion mixture, and parsley in a large bowl; set aside.",
                "time": 0,
            },
            {
                "name": "Combine eggs, half-and-half, gouda, and Parmesan in a medium bowl. Add to bread cube mixture, stir to combine.",
                "time": 0,
            },
            {
                "name": "Spread bread mixture evenly in the prepared baking dish.",
                "time": 0,
            },
            {
                "name": "Bake until center of bread pudding is set, top is golden brown and a knife inserted in the center comes out clean (71 degrees C internal temperature)",
                "time": 2700,
            },
        ],
        "name": "Stuffing Bread Pudding",
        "servings": 6,
        "tags": ["Side Dish"],
        "time": 60,
    },
    {
        "name": "Cowboy Casserole",
        "info": "This hearty cowboy casserole is comfort food at its best with a creamy filling and crispy tots.",
        "imageUrl": "https://www.allrecipes.com/thmb/zUzRfnG8jnVxSs0lZvBIHvFyvY8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Cowboy-Casserole-ddmfs-3x2-274-9a10c12cf35349f6943322d5ab23b98a.jpg",
        "ingredients": [
            "2 slices thick-cut bacon, chopped",
            "1 cup chopped yellow onion",
            "1 cup chopped red bell pepper",
            "1 pound ground sirloin",
            "8 ounces hot pork country sausage",
            "2 teaspoons chopped garlic",
            "1 (10.75 ounce) can condensed cream of mushroom soup",
            "0.5 cup whole milk",
            "0.25 cup sour cream",
            "0.5 teaspoon kosher salt",
            "0.5 teaspoon black pepper",
            "1 cup frozen corn kernels",
            "1.5 cups shredded extra-sharp Cheddar cheese, divided",
            "1 (32 ounce) package frozen tater tots",
            "2 tablespoons chopped fresh flat-leaf parsley",
        ],
        "time": 55,
        "tags": ["Dinner"],
        "instructions": [
            {
                "name": "Preheat the oven to 190 degrees with a rack in the center position.",
                "time": 0,
            },
            {"name": "Heat a large cast-iron skillet over medium heat.", "time": 0},
            {
                "name": "Add bacon and cook, stirring often, until browned and crisp, about 7 minutes.",
                "time": 420,
            },
            {
                "name": "Transfer bacon to a paper towel-lined plate with a slotted spoon, reserving 2 tablespoons of the drippings.",
                "time": 0,
            },
            {
                "name": "Add chopped onion and red bell pepper to the drippings in the skillet; cook, stirring occasionally, until softened, about 4 minutes.",
                "time": 240,
            },
            {
                "name": "Increase heat to medium-high and add ground sirloin and hot pork country sausage. Cook, stirring, until beef is crumbly, browned, and no longer pink, 6 to 8 minutes.",
                "time": 360,
            },
            {
                "name": "Add chopped garlic and cook, stirring constantly, until fragrant, about 1 minute.",
                "time": 60,
            },
            {
                "name": "Remove skillet from heat and drain excess fat, if desired.",
                "time": 0,
            },
            {
                "name": "Stir in condensed cream of mushroom soup, whole milk, sour cream, kosher salt, and black pepper.",
                "time": 0,
            },
            {
                "name": "Stir in frozen corn, cooked bacon, and 1/2 cup of shredded Cheddar cheese.",
                "time": 0,
            },
            {
                "name": "Sprinkle the top evenly with the remaining 1 cup of shredded Cheddar cheese.",
                "time": 0,
            },
            {
                "name": "Arrange frozen tater tots in concentric circles over the cheese layer (there will be about 1 1/2 cups of tater tots leftover; reserve for another use).",
                "time": 0,
            },
            {
                "name": "Bake in the preheated oven until the top is golden brown and the beef mixture is bubbly, about 35 minutes.",
                "time": 2100,
            },
            {
                "name": "Let the casserole sit for 5 minutes before serving.",
                "time": 300,
            },
            {
                "name": "Sprinkle with chopped fresh flat-leaf parsley and serve hot.",
                "time": 0,
            },
        ],
        "servings": 8,
        "difficulty": "easy",
    },
    {
        "name": "Churro Bundt Cake",
        "info": "This cinnamon-flavored churro Bundt cake is topped with dulce de leche— a truly stunning dessert.",
        "imageUrl": "https://www.allrecipes.com/thmb/8czqevRbrO95cBlq4jwePKtm68I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/7972536-churro-bundt-cake-ddmfs-4x3-809d618f200749949b1cc8af9a8bc721.jpg",
        "ingredients": [
            "1 cup salted butter, softened",
            "3 tablespoons butter, melted",
            "2 1/2 cups all-purpose flour",
            "1 1/4 cup white sugar, divided",
            "1/3 cup packed brown sugar",
            "1 tablespoon vanilla extract",
            "3 eggs",
            "2 egg yolks",
            "1 tablespoon baking powder",
            "1/2 teaspoon salt",
            "2 tablespoons plus 2 teaspoons ground cinnamon",
            "1 cup milk",
            "For topping (optional):",
            "1/3 cup purchased dulce de leche",
            "1 tablespoon milk",
        ],
        "time": 45,
        "tags": ["Dessert"],
        "instructions": [
            {"name": "Gather all ingredients.", "time": 0},
            {
                "name": "Preheat oven to 175 degrees C. Grease and flour a 10-inch fluted tube pan; set aside.",
                "time": 0,
            },
            {
                "name": "In a large bowl, beat 1 cup softened butter with an electric mixer on medium speed for 30 seconds.",
                "time": 0,
            },
            {
                "name": "Add 1 cup white sugar, brown sugar, and vanilla; beat for 4 to 5 minutes or until light and fluffy.",
                "time": 0,
            },
            {"name": "Add eggs and egg yolks; beat for 1 minute.", "time": 60},
            {
                "name": "In a separate bowl, whisk together flour, baking powder, salt, and 2 tablespoons plus 2 teaspoons of ground cinnamon.",
                "time": 0,
            },
            {
                "name": "Alternately add the flour mixture and milk to the butter mixture, beating on low speed after each addition just until combined, scraping the sides of the bowl as needed.",
                "time": 0,
            },
            {"name": "Spoon the batter into the prepared pan.", "time": 0},
            {
                "name": "Bake until a toothpick inserted in the center comes out clean, 45 to 50 minutes.",
                "time": 2700,
            },
            {
                "name": "Cool the cake in the pan on a wire rack for 10 minutes. Then, remove the cake from the pan and cool completely on a wire rack.",
                "time": 600,
            },
            {
                "name": "In a bowl, mix together 1/4 cup white sugar and 2 teaspoons of ground cinnamon for the topping.",
                "time": 0,
            },
            {
                "name": "Brush a small section of the cake with 3 tablespoons melted butter and sprinkle with the cinnamon sugar mixture. Repeat with the remaining sections until the cake is fully covered.",
                "time": 0,
            },
            {
                "name": "For the topping, if using, mix dulce de leche and milk in a microwave-safe bowl and microwave for 30 seconds or until the mixture is of drizzling consistency.",
                "time": 30,
            },
            {"name": "Drizzle the topping over the cooled cake.", "time": 0},
        ],
        "servings": 12,
        "difficulty": "medium",
    },
    {
        "name": "Marry Me Chicken",
        "info": "Marry me chicken is sautéed chicken in a creamy sun-dried tomato sauce, served alone or with pasta. Either way, it's worthy of a marriage proposal!",
        "imageUrl": "https://www.allrecipes.com/thmb/4B9LUoqPVUQXzGWgrBdVuECH-2I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/275590-marry-me-chicken-DDMFS-4x3-1689-web-5363b11b1bf5493c923d63d083cc4b52.jpg",
        "ingredients": [
            "1.5 pounds skinless, boneless chicken breast halves",
            "2 tablespoons butter",
            "3 cloves garlic, minced",
            "0.5 teaspoon dried oregano",
            "0.25 teaspoon ground thyme",
            "0.5 cup chicken broth, divided",
            "0.5 pound bacon",
            "1 (16 ounce) package angel hair pasta",
            "1 tablespoon all-purpose flour",
            "0.5 cup freshly shaved Parmesan cheese",
            "0.25 cup whipping cream",
            "0.25 cup chopped sun-dried tomatoes",
            "1 pinch red pepper flakes",
            "salt to taste",
        ],
        "time": 20,
        "tags": ["Dinner"],
        "instructions": [
            {
                "name": "Gather ingredients. Preheat the oven to 350 degrees F (175 degrees C).",
                "time": 0,
            },
            {
                "name": "Place chicken breasts on a flat work surface. Slice horizontally through the middle, being careful not to cut all the way through to the other side. Open the 2 sides and spread them out like an open book to butterfly.",
                "time": 0,
            },
            {
                "name": "Melt butter in a large, oven-safe skillet over medium-high heat. Add garlic, oregano, and thyme. Sauté until fragrant, about 30 seconds.",
                "time": 30,
            },
            {
                "name": "Add chicken and cook until golden brown but not fully cooked, 3 to 4 minutes per side.",
                "time": 360,
            },
            {
                "name": "Pour 1/4 cup chicken broth into the skillet and bake in the preheated oven until chicken is no longer pink in the centers and juices run clear, about 15 minutes.",
                "time": 900,
            },
            {
                "name": "Meanwhile, place bacon in a large skillet and cook over medium-high heat, turning occasionally, until evenly browned, about 10 minutes.",
                "time": 600,
            },
            {
                "name": "Drain bacon slices on paper towels and let cool enough to handle, about 5 minutes; chop.",
                "time": 300,
            },
            {
                "name": "At the same time, bring a large pot of lightly salted water to a boil. Cook angel hair pasta in the boiling water, stirring occasionally, until tender yet firm to the bite, 4 to 5 minutes. Drain and keep warm.",
                "time": 240,
            },
            {
                "name": "Remove skillet from the oven and transfer chicken to a plate, reserving juices in the skillet. Keep chicken warm and place skillet on the stovetop.",
                "time": 0,
            },
            {
                "name": "Whisk flour into the skillet over medium heat. Add remaining chicken broth, Parmesan cheese, and whipping cream. Whisk until combined.",
                "time": 60,
            },
            {
                "name": "Add sun-dried tomatoes, red pepper flakes, and salt. Add bacon and chicken back into the skillet.",
                "time": 0,
            },
            {"name": "Serve on top of hot cooked pasta.", "time": 0},
        ],
        "servings": 6,
        "difficulty": "medium",
    },
    {
        "name": "Yaki Udon",
        "info": "Yaki Udon is a classic Japanese stir-fry dish with lots of vegetables in a soy-based sauce. Feel free to add meat or tofu.",
        "imageUrl": "https://www.allrecipes.com/thmb/mq6dWz5NgkaBUWBts_BBU5QeVJs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/yaki-udon-ddmfs-3x2-55-30ba570fed0a425595f9b1343ebd9c6e.jpg",
        "ingredients": [
            "0.25 cup oyster sauce",
            "3 tablespoons soy sauce",
            "2 tablespoons mirin",
            "1 tablespoon unseasoned rice vinegar",
            "2 teaspoons Worcestershire sauce",
            "2 teaspoons toasted sesame oil",
            "1 teaspoon packed light brown sugar",
            "1 teaspoon Sriracha sauce",
            "1 medium garlic, grated",
            "1 medium (5-oz.) bunch scallions",
            "2 tablespoons canola oil",
            "12 ounces sliced mixed wild mushrooms",
            "2 medium heads baby bok choy, thinly sliced",
            "1 (10 ounce) package carrots, cut into match-stick size pieces",
            "0.5 cup water, divided",
            "1 (14 ounce) package pre-cooked udon noodles",
            "Optional garnishes: thinly sliced nori, cilantro, lime wedges, furikake seasoning",
        ],
        "time": 15,
        "tags": [],
        "instructions": [
            {
                "name": "Whisk together oyster sauce, soy sauce, mirin, rice vinegar, Worcestershire, sesame oil, sugar, Sriracha, and garlic in a small bowl; set aside.",
                "time": 0,
            },
            {
                "name": "Remove root ends from scallions and discard. Chop whites and light greens into 2-inch pieces and quarter pieces lengthwise; set aside. Thinly slice remaining dark greens of scallions and reserve for garnish.",
                "time": 0,
            },
            {
                "name": "Heat oil in a large skillet or wok over medium-high heat. Add mushrooms in a single layer and cook, undisturbed, until browned on first side, about 3 minutes.",
                "time": 180,
            },
            {
                "name": "Stir and continue to cook, stirring occasionally, until mushrooms are tender and golden brown on both sides, about 4 more minutes.",
                "time": 240,
            },
            {
                "name": "Add bok choy, carrots, sliced whites and light greens of scallions, and 1/4 cup water to pan with mushrooms. Cook, stirring occasionally, until vegetables are just tender, about 3 minutes.",
                "time": 180,
            },
            {
                "name": "Add udon noodles and remaining 1/4 cup water. Cook, gently separating noodles with tongs or spoon.",
                "time": 0,
            },
            {
                "name": "Add reserved oyster sauce mixture and cook, stirring constantly, until noodles and vegetables are well-coated, about 1 minute.",
                "time": 60,
            },
            {
                "name": "Divide among serving bowls and garnish with reserved sliced greens of scallions and optional garnishes. Serve immediately.",
                "time": 0,
            },
        ],
        "servings": 4,
        "difficulty": "easy",
    },
    {
        "name": "Macarons",
        "info": "Macarons are crisp French meringue cookies made with almond flour, egg whites, and sugar; sandwich the macarons with buttercream or jam for the perfect sweet treat!",
        "imageUrl": "https://www.allrecipes.com/thmb/uREZ59EyYLaThVDLyA4Eko1Z7eA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1012979-f53fe25d6fc041d1b7b25e36c308bec9.jpg",
        "ingredients": [
            "4 extra large egg whites",
            "1.67 cups confectioners' sugar",
            "1.33 cups almond flour",
            "0.125 teaspoon salt",
            "0.25 cup superfine (castor) sugar",
            "0.25 cup seedless raspberry jam",
        ],
        "time": 20,
        "tags": ["Dessert"],
        "instructions": [
            {
                "name": "Chill egg whites in a metal mixing bowl overnight. The next day, bring them to room temperature.",
                "time": 0,
            },
            {
                "name": "Preheat oven to 280°F (138°C). Line two baking sheets with parchment paper.",
                "time": 0,
            },
            {
                "name": "Whisk confectioners' sugar and almond flour in a bowl.",
                "time": 0,
            },
            {
                "name": "Beat egg whites with salt until foamy (about 1 minute). Gradually add superfine sugar, beating until stiff peaks form (3-5 minutes on high speed).",
                "time": 240,
            },
            {
                "name": "Gently fold almond flour mixture into whipped egg whites. Spoon meringue into a pastry bag with a 3/8-inch tip. Pipe 1-inch disks onto prepared baking sheets, leaving 2 inches of space between them.",
                "time": 0,
            },
            {
                "name": "Tap baking sheets to remove air bubbles. Let macarons sit at room temperature until the surfaces become dull and a thin skin forms (25-30 minutes).",
                "time": 1500,
            },
            {
                "name": "Bake until macarons are dry (about 19-20 minutes). Cool completely on baking sheets.",
                "time": 1200,
            },
            {"name": "Spread half of the macarons with raspberry jam.", "time": 0},
            {
                "name": "Top with remaining macarons to make sandwich cookies.",
                "time": 0,
            },
            {
                "name": "Refrigerate for at least 2 hours to let them soften before serving.",
                "time": 0,
            },
        ],
        "servings": 15,
        "difficulty": "medium",
    },
    {
        "name": "Grilled Okra and Grape Tomatoes",
        "info": "Okra and grape tomatoes are skewered and grilled—an easy grilled side perfect for end-of-summer cookouts.",
        "imageUrl": "https://www.allrecipes.com/thmb/O63l0410rw8QxCc1mwfP275aXiE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/7506789-Grilled-Okra-and-Grape-Tomatoes-GOLDMAN-4x3-3634-f29d64dcbf4e4a5797af0b00169345e6.jpg",
        "ingredients": [
            "32 okra pods",
            "32 grape tomatoes",
            "1/2 teaspoon salt-free Cajun seasoning",
            "1 tablespoon canola oil",
            "1/2 teaspoon kosher salt",
            "1/2 teaspoon black pepper",
        ],
        "time": 5,
        "tags": ["Dinner"],
        "instructions": [
            {
                "name": "Soak 8 (8-inch) wooden skewers in water for 30 minutes.",
                "time": 1800,
            },
            {
                "name": "Preheat an outdoor grill to high heat 200 to 230 degrees C. Lightly oil grill.",
                "time": 0,
            },
            {
                "name": "Thread 4 okra pods and 4 grape tomatoes onto each soaked skewer.",
                "time": 0,
            },
            {
                "name": "Stir together Cajun seasoning and canola oil in a small bowl; brush onto okra and tomatoes. Sprinkle with kosher salt and black pepper.",
                "time": 0,
            },
            {
                "name": "Grill vegetable skewers, turning halfway through, until okra is bright green and tender and grill marks form, 6 to 8 minutes.",
                "time": 420,
            },
            {
                "name": "Transfer okra and tomatoes from skewers into a serving bowl.",
                "time": 0,
            },
        ],
        "servings": 4,
        "difficulty": "easy",
    },
]


@app.get("/recipe/")
def read_item(url: str):
    if not url:
        return {"error": "url is required"}
    scraper = scrape_me(url)
    json = scraper.to_json()
    return restructure_recipe(json)


@app.get("/recipes/")
def get_recipes():
    # recipes = []
    # for url in recipes_urls:
    #     json = read_item(url)
    #     recipes.append(json)
    return recipes_json


def restructure_recipe(recipe: dict) -> dict:
    new_recipe = {}
    new_recipe["name"] = recipe["title"]
    new_recipe["info"] = recipe["description"]
    new_recipe["imageUrl"] = recipe["image"]
    new_recipe["ingredients"] = recipe["ingredients"]
    new_recipe["time"] = recipe["cook_time"]
    new_recipe["tags"] = []
    category = recipe["category"]
    if category:
        new_recipe["tags"].append(recipe["category"])

    # convert instructions_list to list of objects (name, time=0 )
    new_recipe["instructions"] = []
    for instruction in recipe["instructions_list"]:
        new_recipe["instructions"].append({"name": instruction, "time": 0})
    # split splace and try to get number
    yields = recipe["yields"]
    yield_number = yields.split(" ")[0]
    if yield_number.isdigit():
        new_recipe["servings"] = int(yield_number)
    else:
        new_recipe["servings"] = 1
    new_recipe["difficulty"] = difficulty_calc(len(new_recipe["instructions"]))
    return new_recipe


def difficulty_calc(instructionsNum) -> str:
    if instructionsNum < 6:
        return "easy"
    elif instructionsNum < 15:
        return "medium"
    else:
        return "hard"

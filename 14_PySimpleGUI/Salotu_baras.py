import PySimpleGUI as sg

class SaladBarApp:
    def __init__(self):
        self.recipe_manager = RecipeManager()
        self.cost_calculator = CostCalculator()
        self.salad_bar = SaladBar(self.recipe_manager, self.cost_calculator)
        self.manager = Manager()
        self.salad_choices = list(self.recipe_manager.get_all_recipes().keys())[:3]


    def create_main_layout(self):
        salad_choices = list(self.recipe_manager.get_all_recipes().keys())[:3]
        
        if not salad_choices:
            print("Error: No salad choices available")
       
            
        return [
            [sg.Text("Sveiki atvykę į SaladBar!", font="Verdana 15")],
            [sg.Text("Pasirinkite savo salotą:", font="Verdana 12")],
            [
                sg.Radio(salad_choices[0], "SALAD", key="-SALAD1-", default=True, font="Terminal 12"),
                sg.Radio(salad_choices[1], "SALAD", key="-SALAD2-", font="Terminal 12"),
                sg.Radio(salad_choices[2], "SALAD", key="-SALAD3-", font="Terminal 12"),
            ],
            [sg.Image(filename='path_to_salad_image1.png', key='-IMAGE1-')],
            [sg.Image(filename='path_to_salad_image2.png', key='-IMAGE2-')],
            [sg.Image(filename='path_to_salad_image3.png', key='-IMAGE3-')],
            [sg.Text("Papildomos pasirinkimai:", font="Verdana 12")],
            [
                sg.Checkbox("Pridėti pomidorų", key="-TOMATO-", font="Terminal 12"),
                sg.Checkbox("Pridėti agurkų", key="-CUCUMBER-", font="Terminal 12"),
            ],
            [sg.Button("Užsisakyti", key="-ORDER-", font="Verdana 12")],
            [sg.Text(size=(40, 1), key="-OUTPUT-", font="Verdana 15")],
        ]

    def create_manager_layout(self):
        return [
            [sg.Text("Vadovo prieiga", font="Verdana 15")],
            [sg.Input("Įveskite kodą", key="-CODE-", font="Terminal 15")],
            [sg.Button("Patvirtinti", key="-CONFIRM-", font="Verdana 12")],
            [sg.Text(size=(40, 1), key="-MANAGER-OUTPUT-", font="Verdana 15")],
        ]

    def run(self):
        main_layout = self.create_main_layout()
        manager_layout = self.create_manager_layout()

        window = sg.Window("SaladBar", main_layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == "-ORDER-":
                recipe_name = values["-RECIPE-"]
                extras = []
                if values["-TOMATO-"]:
                    extras.append({"name": "Pomidorai", "price": 1.0})
                if values["-CUCUMBER-"]:
                    extras.append({"name": "Agurkai", "price": 0.5})

                result = self.salad_bar.create_order(recipe_name, extras)
                window["-OUTPUT-"].update(result, text_color="#99ff99")

            if event == "-CONFIRM-":
                code = values["-CODE-"]
                if self.manager.access_manager_portal(code):
                    window.close()
                    manager_window = sg.Window("Manager Panel", manager_layout)
                    while True:
                        manager_event, manager_values = manager_window.read()

                        if manager_event == sg.WINDOW_CLOSED:
                            break

                        # Čia galite pridėti kodą, skirtą vadovui

                    manager_window.close()
                else:
                    window["-MANAGER-OUTPUT-"].update("Neteisingas kodas", text_color="#ff9999")

        for i, salad_choice in enumerate(self.salad_choices, start=1):
            if values[f"-SALAD{i}-"]:
                window[f"-IMAGE{i}-"].update(filename=f'path_to_salad_image{i}.png')
            else:
                window[f"-IMAGE{i}-"].update(filename='')

        window.close()
  
class RecipeManager:
    def __init__(self):
        self.recipes = {
            "Cezario salotos": {"Romaninės salotos": 200, "Vyšniniai pomidorai": 100, "Putpelės kiaušiniai": 50, "Kietasis sūris": 75},
            "Ožkos sūrio salotos": {"Romaninės salotos": 150, "Pomidorai": 100, "Mėlynasis svogūnas": 50, "Kepamas ožkos sūris su pelėsiu": 100},
            "Skumbrės salotos": {"Garbatonos salotos": 150, "Marinuotas mėlynas svogūnas": 50, "Virtos ir keptos bulvės": 100, "Marinuoti agurkai": 50},
        }

    def add_recipe(self, name, ingredients):
        self.recipes[name] = ingredients

    def get_all_recipes(self):
        return self.recipes


 
class CostCalculator:
    def __init__(self):
        self.ingredients_cost = {}

    def add_ingredient_cost(self, ingredient, cost_per_gram):
        self.ingredients_cost[ingredient] = cost_per_gram

    def calculate_cost(self, recipe):
        total_cost = 0
        for ingredient, quantity in recipe.items():
            total_cost += quantity * self.ingredients_cost.get(ingredient, 0)
        return total_cost

class SaladBar:
    def __init__(self, recipe_manager, cost_calculator):
        self.recipe_manager = recipe_manager
        self.cost_calculator = cost_calculator
        self.orders = {}

    def create_order(self, recipe_name, extras=[]):
        recipe = self.recipe_manager.get_all_recipes().get(recipe_name, {})
        if not recipe:
            return "Recipe not found"

        total_cost = self.cost_calculator.calculate_cost(recipe)

        for extra in extras:
            total_cost += extra.get("price", 0)

        order_number = len(self.orders) + 1
        self.orders[order_number] = {"recipe": recipe_name, "total_cost": total_cost}
        return f"Order placed. Order Number: {order_number}. Total Cost: {total_cost}"

class Manager:
    def __init__(self):
        self.access_code = "1234"

    def access_manager_portal(self, code):
        return code == self.access_code

# Pavyzdinė programos naudojimo dalis:

# Sukuriame receptų valdytoją
recipe_manager = RecipeManager()
recipe_manager.add_recipe("Cezario salotos", {"Romaninės salotos": 200, "Vyšniniai pomidorai": 100, "Putpelės kiaušiniai": 50, "Kietasis sūris": 75})
recipe_manager.add_recipe("Ožkos sūrio salotos", {"Romaninės salotos": 150, "Pomidorai": 100, "Mėlynasis svogūnas": 50, "Kepamas ožkos sūris su pelėsiu": 100})
recipe_manager.add_recipe("Skumbrės salotos", {"Garbatonos salotos": 150, "Marinuotas mėlynas svogūnas": 50, "Virtos ir keptos bulvės": 100, "Marinuoti agurkai": 50})

# Sukuriame kainų skaičiuotoją
cost_calculator = CostCalculator()
cost_calculator.add_ingredient_cost("Romaninės salotos", 0.5)
cost_calculator.add_ingredient_cost("Vyšniniai pomidorai", 1.0)
# Pridėkite kainas ir kitiems ingredientams

# Sukuriame salotų barą
salad_bar = SaladBar(recipe_manager, cost_calculator)

# Sukuriame vadovo prieigą
manager = Manager()
salad_choices = list(recipe_manager.get_all_recipes().keys())[:3]

print("Recipes:", recipe_manager.get_all_recipes())

# Vadovo prieiga
access_code = input("Enter manager access code: ")
if manager.access_manager_portal(access_code):
    # Čia galite pridėti kodą, skirtą vadovui
    pass
else:
    # Čia galite pridėti kodą, skirtą klientui
    pass


# Sukurkime aplikaciją ir paleiskime ją
app = SaladBarApp()
app.run()

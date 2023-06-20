import unittest
from rms import RecipeManager, Recipe
from unittest.mock import patch


class TestRecipeManager(unittest.TestCase):

    print("First Test Recipe Management System")

    def test_import_recipe(self):
        print("")
        print("Testing importing recipe file")
        print("")
        self.manager = RecipeManager()
        self.manager.import_data(file_path='recipes.csv')
        self.assertEqual(len(self.manager.recipes), 5)

    def test_export_recipe(self):
        print("")
        print("Testing exporting recipe file")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.manager.export_data(file_format='csv')

    @patch('builtins.input', side_effect=["kunafa", "cream honey cheese sugar syrup",
                                          "1) mix evrything and boom", "dessert", "3"])
    def test_add_recipe(self, mock_input):
        print("")
        print("Testing Adding a Recipe")
        print("")
        self.manager = RecipeManager()
        self.manager.add_recipe()
        self.assertEqual(len(self.manager.recipes), 1)

    @patch('builtins.input', side_effect=["500"])
    def test_delete_recipe(self, mock_input):
        print("")
        print("Testing Deleting a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.manager.delete_recipe()
        self.assertEqual(len(self.manager.recipes), 0)

    @patch('builtins.input', side_effect=["500", "sherbet", "milk rose syrup tadpoles",
                                          "1) mix evrything and boom", "refereshener", "4"])
    def test_edit_recipe(self, mock_input):
        print("")
        print("Testing editing a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)
        self.assertTrue(self.manager.edit_recipe())

    @patch('builtins.input', side_effect=["1", "4", "kunafa", "3", "dessert", "2", "5"])

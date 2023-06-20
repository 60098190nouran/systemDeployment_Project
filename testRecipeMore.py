import unittest
from rms import RecipeManager, Recipe
from unittest.mock import patch


class TestRecipeManager(unittest.TestCase):

    print("Second Test Recipe Management System (Testing Raising Exception Only)")

    @patch('builtins.input', side_effect=["", "", "", "", ""])
    def test_add_recipe(self, mock_input):
        # Let the fields remain empty for testing exception
        print("")
        print("Testing Adding a Recipe")
        print("")
        self.manager = RecipeManager()
        with self.assertRaises(Exception):
            self.manager.add_recipe()

    @patch('builtins.input', side_effect=[""])
    def test_delete_recipe(self, mock_input):
        # Trying to delete a non existent recipe
        print("")
        print("Testing Deleting a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)

        with self.assertRaises(Exception):
            self.manager.delete_recipe()  # Enter ID of non existent recipe

    @patch('builtins.input', side_effect=["", "", "", "", "", ""])
    
    def test_edit_recipe(self, mock_input):
        # Trying to update a non existent recipe
        print("")
        print("Testing updating a Recipe")
        print("")
        test_recipe = Recipe(500, "kunafa", "cream honey cheese sugar syrup",
                             "1) mix evrything and boom", "dessert", "3")
        self.manager = RecipeManager()
        self.manager.recipes.append(test_recipe)

        with self.assertRaises(Exception):
            self.manager.edit_recipe()  # Enter ID of non existent recipe


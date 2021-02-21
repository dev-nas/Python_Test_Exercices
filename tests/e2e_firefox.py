import unittest
from selenium import webdriver
# configuration du navigateur pour la session firefox
from selenium.webdriver.firefox.options import Options

class PythonOrgSearch(unittest.TestCase):
    
    # on va lancer une session Firefox
    def setUp(self):
        # mode sans fenêtre
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Firefox(options=opts)
        # charger une URL
        self.driver.get("http://www.python.org")
    
    @unittest.skip
    def test_search_title(self):
        assert "Welcome to Python.org" in self.driver.title
    
    def test_search_widget(self):
        # sélectionner un élément seln un attribut ou autre
        element = self.driver.find_element_by_name("q")
        # simuler une écriture dans le champ input
        element.send_keys("Pycon")
        # trouver le bouton de soumission de la recherche
        btn = self.driver.find_element_by_id("submit")
        # cliquer dessus
        btn.click()
        # vérifier qu"on a la réponse attendue
        assert "No results found." not in self.driver.page_source
    
    # fermer les connections
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
import unittest
import sqlite3

class Test(unittest.TestCase):

    def setUp(self):

        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)")

    def test_inserir_usuario(self):

        self.cursor.execute("INSERT INTO usuarios (nome) VALUES ('Maria')")
        self.conn.commit()

        self.cursor.execute("SELECT nome FROM usuarios WHERE id = 2")
        usuario = self.cursor.fetchone()
        self.assertEqual(usuario[1], 'Maria')

    def tearDown(self):
        return super().tearDown()
    
if __name__ == '__main__':
    unittest.main()

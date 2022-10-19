import unittest
from unittest.mock import patch
from src.pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Otavio', 'Martins')
        
    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Otavio') 
        
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        
    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Martins') 
        
    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        
    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        
    def test_obter_todos_os_dados_com_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)
            
    def test_obter_todos_os_dados_com_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)
        
    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)
            
            fake_request.return_value.ok = False
            
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
        